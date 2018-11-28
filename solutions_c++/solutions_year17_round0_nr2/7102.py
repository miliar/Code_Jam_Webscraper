#include <iostream>
#include <string>
#include <climits>
#include <vector>

using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;

const unsigned int SIZE = 20;

void doCase(int caseNum) {
    unsigned long N;
    cin >> N;
    vector<unsigned int> n(SIZE);

    int idx = SIZE - 1;
    unsigned long w = N;
    while (w > 0) {
        if (idx < 0) {
            cout << "ERROR: couldn't fit " << N << " in " << SIZE << " digits" << endl;
            break;
        }
        n[idx] = w % 10;
        w = w / 10;
        idx--;
    }

    bool good = false;
    while (!good) {
        good = true;
        int curr = 0;
        for (int pos = 0; pos < n.size(); pos++) {
            unsigned int d = n[pos];
            if (d < curr) {
                good = false;
                for (int j = pos; j < n.size(); j++) {
                    n[j] = 9;
                }
                for (int j = pos - 1; j >= 0; j--) {
                    if (n[j] == 0) {
                        n[j] = 9;
                    } else {
                        n[j] = n[j] - 1;
                        break;
                    }
                }
                break;
            } else {
                curr = d;
            }
        }
    }

    cout << "Case #" << caseNum << ": ";
    bool started = false;
    for (int i = 0; i < n.size(); i++) {
        if (n[i] != 0 || started) {
            cout << n[i];
            started = true;
        }
    }
    cout << endl;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++) {
        doCase(i+1);
    }
}
