"""
Purpose: To calculate running median from input file
@Author: Rohan gudgila
"""
from datetime import datetime
from collections import OrderedDict
import sys

from build_min_max_heap import BuildMinMaxHeap


class Donor:
    list_donor = {}

    def __init__(self):
        self.small = []
        self.large = []
        self.count = 1
        self.median = 0
        self.tot_trans = 0

    # calculates the median, total count of transaction and total amount per id based on the key
    def compute_med_count_amount(self, heap_id, trans_amt):
        if self.list_donor.get(heap_id):
            self.small = self.list_donor.get(heap_id)[0]
            self.large = self.list_donor.get(heap_id)[1]
            self.count = self.list_donor.get(heap_id)[3] + 1
            self.tot_trans = self.list_donor.get(heap_id)[4] + int(trans_amt)
        else:
            self.tot_trans = int(trans_amt)
            self.list_donor[heap_id] = [self.small, self.large, self.median, self.count, self.tot_trans]
        (s1, l1) = BuildMinMaxHeap.build_heap(self.small, self.large , int(trans_amt))
        # Updating values in the dictionary for the given key
        self.list_donor.get(heap_id)[0] = s1
        self.list_donor.get(heap_id)[1] = l1
        self.list_donor.get(heap_id)[3] = self.count
        self.list_donor.get(heap_id)[4] = self.tot_trans
        # Calculating median based on the min, max heap
        if len(s1) == len(l1):
            temp = (l1[0] - s1[0]) / 2.0
            self.list_donor.get(heap_id)[2] = int(round(temp)) # rounding up the number if > 0.5
        else:
            self.list_donor.get(heap_id)[2] = -int(s1[0]) if len(s1) > len(l1) else int(l1[0])
        return self.list_donor.get(heap_id)[2], self.count, self.tot_trans


class FindPoliticalDonors:
    def __init__(self):
        pass

    final_list_dt = OrderedDict()
    final_list_zip = OrderedDict()

    '''
        The input format of the file is:
        C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783
        Each column is "|" separated. Columns of interest are  cmte_id (1st col), zip_code(11th col), transaction_date(14th col),
        transaction_amount(15th col) and Other_id(16th col)
    '''
    # Reading the input file content
    def read_data(self, fin):
        with open(fin) as f:
            content = f.readlines()
        for c in content:
            col = c.split("|")
            # if other_id is not empty or (cmte_id or transaction_amt) is empty
            if not col[15] and col[0] and col[14]:
                        self.build_zip_date_dict(col[0], col[10], col[13], col[14])

    # Writing to the output file
    @staticmethod
    def write_file(fname, dict):
        output = open(fname, "w")
        for k, v in dict.items():
            output.write("%s\n" % v)

    # check if the date is in valid format: Expected format is mmddyyyy
    @staticmethod
    def validate_date(d):
        try:
            datetime.strptime(d, '%m%d%Y')
            return True
        except ValueError:
            return False

    # building the final dictionary to output it to zip and date text files.
    def build_zip_date_dict(self, cmte_id, zip_code, trans_dt, trans_amt):
        # flag indicates whether data should be considered for computation of respective median
        flag_zip = True
        flag_dt = True
        if not trans_dt or not FindPoliticalDonors.validate_date(trans_dt):
            flag_dt = False
        if not zip_code or len(zip_code) < 5:
            flag_zip = False
        # zip code should be stripped to five digits if length is > 5
        if len(zip_code) > 5:
            zip_code = zip_code[:5]
        if flag_dt:
            # For calculation of medianvals_by_date.txt id is : cmteid|transaction_date|count
            key = cmte_id + "|" + trans_dt
            (med, count, t_trans) = Donor().compute_med_count_amount(key, trans_amt)
            self.final_list_dt[key] = key + "|" + str(med) + "|" + str(count) + "|" + str(t_trans)
        if flag_zip:
            # For calculation of medianvals_by_zip.txt id is : cmteid|zip_code
            key = cmte_id + "|" + zip_code
            (med, count, t_trans) = Donor().compute_med_count_amount(key, trans_amt)
            s_count = str(count)
            self.final_list_zip[key + "_" + s_count] = key + "|" + str(med) + "|" + s_count+ "|" + str(t_trans)


def main():
    if len(sys.argv) != 4:
        print "Provide proper number of arguments to the script"
        return
    input_filename = sys.argv[-3]
    output_zip_filename = sys.argv[-2]
    output_dt_filename = sys.argv[-1]
    fp = FindPoliticalDonors()
    FindPoliticalDonors().read_data(input_filename)
    FindPoliticalDonors.write_file(output_zip_filename, fp.final_list_zip)
    FindPoliticalDonors.write_file(output_dt_filename, fp.final_list_dt)


if __name__ == '__main__':
    main()


