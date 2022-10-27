import csv
import sys
import random


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # TODO: Read DNA sequence file into a variable

    sed = open(sys.argv[2], "r")
    se = sed.read()

    # TODO: Read database file into a variable
    dt = []
    fl = open(sys.argv[1], "r")
    reader = csv.DictReader(fl)
    header = reader.fieldnames[1::]
    for row in reader:
        dt.append(row)

    found = {}
   # TODO: Find longest match of each STR in DNA sequence
    for str in header:
        found[str] = longest_match(se, str)

    # TODO: Check database for matching profiles
    for per in dt:
        m = 0
        for str in header:

            if int(per[str]) == found[str]:

                m = m + 1

        if m == len(header):
            print(per["name"])
            fl.close()
            return
    print("No match")
    return


def longest_match(se, str):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variablesv
    longest_run = 0
    subsequence_length = len(str)
    sequence_length = len(se)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if se[start:end] == str:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)
    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

