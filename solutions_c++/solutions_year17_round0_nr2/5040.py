#include <iostream>
#include <fstream>
using namespace std;

int
main() {
    //fstream in("input.sample");
    //fstream in("B-small-attempt0.in");
    fstream in("B-large.in");

    ofstream out("result.txt");

    int nbTest;
    string str;
    in >> nbTest;
    for (int i = 1; i <= nbTest; ++i) {
        in >> str;

        int digits[str.length()];

        for (int j = 0; j < str.length(); ++j) {
            digits[j] = str.at(j) - '0';
        }

        for(int j = str.length() - 1; j > 0 ; j--) {
            if (digits[j-1] > digits[j] ) {
                digits[j] = 9;
                digits[j-1] = digits[j-1] - 1;
            }
        }



        {
            out << "Case #" << i << ": " ;
            int j;
            for (j = 0; j < str.length() - 1; ++j) {
                if (digits[j] != 0) {
                    break;
                }
            }
            bool madeTo9 = false;
            for (; j < str.length(); ++j) {
                if (madeTo9) {
                    out << 9;
                } else {
                    if (digits[j] == 9) {
                        madeTo9 = true;
                    }
                    out << digits[j];
                }
            }
            out << endl;
        }

        {
            cout << "Case #" << i << ": " ;
            int j;
            for (j = 0; j < str.length() - 1; ++j) {
                if (digits[j] != 0) {
                    break;
                }
            }
            bool madeTo9 = false;
            for (;j < str.length(); ++j) {
                if (madeTo9) {
                    cout << 9;
                } else {
                    if (digits[j] == 9) {
                        madeTo9 = true;
                    }
                    cout << digits[j];
                }
            }
            cout << endl;
        }
    }

    return 0;
}
