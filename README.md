

The project run on version of python 2.7 or above
Below is my problem approach:
i) Read the content of file line by line
ii) Consider the lines for computation based on restriction mentioned in the problem
iii) For calculating the median of the file, create a min/max heap for each id (where id is combination of cmte_id, transaction_date for
medianvals_by_date.txt and combination of cmte_id, zip_code, total number of transaction for medianvals_by_zip.txt)
iv) After caluclatin the median, total_amont and count of transaction output the final results to two files
