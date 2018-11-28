/*
 *  Copyright (C) 2017 by Protein Metrics Inc. - All Rights Reserved.
 *  Unauthorized copying or distribution of this file, via any medium is strictly prohibited.
 *  Confidential.
 *
 *  Author  : Yashpalsinh Gohil (yash.gohiil@gmail.com)
 */
#include <QCoreApplication>
#include <iostream>

using namespace std;

void displayFlips(string panString, int flip, int testCaseNumber) {
    int attemptToFlip = 0;
    size_t position = 0;
    size_t length = panString.length();

    while ((position = panString.find("-", position)) != std::string::npos) {
        if ( (position + flip) <= length ) {
            int start = position;
            int end = position + flip;
            for (; start < end; ++start) {
                if (panString[start] == '+') {
                    panString[start] = '-';
                } else {
                    panString[start] = '+';
                }
            }
            ++attemptToFlip;
        } else {
            break;
        }
        ++position;
    }

    cout << "Case #" << testCaseNumber << ": ";

    if (panString.find("-", position) != std::string::npos) {
        cout << "IMPOSSIBLE" << std::endl;
    } else {
        cout << attemptToFlip << std::endl;
    }
}

int main(int argc, char *argv[])
{
    int totalTestCase;
    cin >> totalTestCase;

    if(totalTestCase <= 100) {
        for (int index = 0; index < totalTestCase; ++index) {
            string panString;
            int flip;

            cin >> panString;
            cin >> flip;

            unsigned int length = panString.length();
            if (length >= 2 && length <= 1000) {
                displayFlips(panString, flip, index +1);
            }
        }
    }
    return 0;
}
