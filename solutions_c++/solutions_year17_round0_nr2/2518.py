#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

bool isTidy(const string& n) {
    if (n.empty()) {
        return true;
    }
    char lowerBound = n[0];
    for (char c : n) {
        if (c < lowerBound) {
            return false;
        }
        lowerBound = c;
    }
    return true;
}

void subtract(string& n, size_t digit) {
    switch (n[digit]) {
        case '0': {
            // need to propagate forward
            n[digit] = '9';
            // assumes there's a higher digit
            subtract(n, digit - 1);
            break;
        }
        case '1': {
            n[digit] = '0';
            break;
        }
        default:
            --n[digit];
            break;
    }
}

string& dynamicProgramming(string& n, size_t head) {
    vector<bool> reduced(n.size(), false);

    while (head < n.size() - 1) {
        // all is fine, none-descending, check next digit
        if (n[head] <= n[head + 1]) {
            ++head;
            continue;
        }
        // if we're the first digit, then we can guarantee next largest tidy number
        if (head == 0 && n[head] == '1') {
            n = string(n.size() - 1, '9');
            return n;
        }

        // { cout << n << " reduced to "; }
        // else n[head+1] needs to be set to 9 and n[head] subtracted
        n[head + 1]       = '9';
        reduced[head + 1] = true;
        if (reduced[head] == false) {
            subtract(n, head);
        }

        // { cout << n << endl; }
        // might've changed the previous digit ordering, so check that
        if (head != 0) {
            --head;
        }
    }
    return n;
}

string bruteForce(string n) {
    while (isTidy(n) == false) {
        // { cout << n << endl; }
        // subtract
        subtract(n, n.size() - 1);
    }
    return n;
}

int main() {
    int T;
    cin >> T;

    for (int c = 1; c <= T; ++c) {
        // integer
        string n;
        cin >> n;

        auto tidyN = dynamicProgramming(n, 0);
        // remove leading 0's
        tidyN.erase(0, min(tidyN.find_first_not_of('0'), tidyN.size() - 1));
        cout << "Case #" << c << ": " << tidyN << endl;
    }
}