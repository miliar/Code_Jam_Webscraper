/*
 *  Copyright (C) 2017 by Protein Metrics Inc. - All Rights Reserved.
 *  Unauthorized copying or distribution of this file, via any medium is strictly prohibited.
 *  Confidential.
 *
 *  Author  : Yashpalsinh Gohil (yash.gohiil@gmail.com)
 */
#include <iostream>
#include <string>

using namespace std;

long long tideNumber(long long number) {
    long long finalNumber = number;

    if (number > 9) {
        for ( long long start = number; start >0;) {
            long long divider = start;
            int previousReminder = 9;
            string deductString = "";

            bool isTidy = true;
            do {
                int reminder = divider % 10;
                divider = divider/10;

                if ( previousReminder < reminder) {
                    isTidy = false;
                    break;
                }

                deductString.insert(0, to_string(reminder));

                previousReminder = reminder;
            } while (divider > 0);

            if (isTidy) {
                finalNumber = start;
                break;
            }

            long long deduct = stoll(deductString);

            if (0 == deduct) {
                deduct = 1;
            }

            start = start - deduct;
        }
    }

    return finalNumber;
}

int main(int argc, char *argv[])
{
    int totalTestCase;
    cin >> totalTestCase;

    if(totalTestCase <= 100) {
        for (int index = 0; index < totalTestCase; ++index) {
            long long number;

            cin >> number;

            long long limit = pow(10, 18);
            if (number  >= 1 && number <= limit) {
                cout << "Case #" << index + 1 << ": " << tideNumber(number) << std::endl;
            }
        }
    }
    return 0;
}
