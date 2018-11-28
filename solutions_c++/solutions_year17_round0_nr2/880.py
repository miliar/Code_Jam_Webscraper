#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void solveTestCase(string &N);
void fillWithNines(string::iterator it, string::iterator ie);

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        string pancake;
        string N;
        
        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> N;
            fout << "Case #" << count << ": ";
            solveTestCase(N);
            fout << N << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}

void solveTestCase(string &N) {

    unsigned index = 0;
    for (string::iterator it = N.begin(), ie = N.end(); it != ie; ++it) {
        if (it + 1 == ie) break;
        else if (*it > *(it+1)) {
            *it = *it - 1;
            if (*(it+1) == '0') {
                if (*it == '0') {
                    N.erase(0, 1);
                    fillWithNines(N.begin(), N.end());
                } else {
                    for(; it >= N.begin(); it--) {
                        if (*(it-1) > *it) {
                            *(it-1) = *it;
                        } else {
                            break;
                        }
                    }
                    fillWithNines(it+1, ie);
                }
                return;
            } else {
                for(; it >= N.begin(); it--) {
                    if (*(it-1) > *it) {
                        *(it-1) = *it;
                    } else {
                        break;
                    }
                }
                fillWithNines(it+1, ie);
                return;
            }
        }
    }

}

void fillWithNines(string::iterator it, string::iterator ie) {
    for(; it != ie; ++it) {
        *it = '9';
    }
}