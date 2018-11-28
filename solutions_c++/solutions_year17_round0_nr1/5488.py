#include <iostream>
#include <string>
#include <vector>

using namespace std;


void findAnswer(string s, unsigned int k, int& flips)
{
    if (s == "") {
        cout << flips << endl;
        return;
    }

    // flip all K adjacent minuses
    int last = s.size() - k;
    for (int i = 0; i <= last; ++i) {
        bool okToFlip = true;

        for (int j = 0; j < k; ++j) {
            if (s[i + j] == '+') {
                okToFlip = false;
                break;
            }
        }

        if (okToFlip) {
            for (int j = 0; j < k; ++j) {
                s[i + j] = '+';
            }
            flips++;
            i += k - 1;
        }
    }

    // strip plusses on the left side
    int a = s.find_first_not_of("+");
    if (a == string::npos) {
        findAnswer("", k, flips);
        return;
    } else {
        s = s.substr(a);
    }

    // strip plusses on the right side
    int b = s.find_last_not_of("+");
    if (b == string::npos) {
        findAnswer("", k, flips);
        return;
    } else {
        s.erase(b + 1);  // ???
    }

    if (s == "") {
        findAnswer(s, k, flips);
        return;
    }

    int num_first_adj_negatives = s.find_first_not_of("-");
    if (num_first_adj_negatives == string::npos) {
        num_first_adj_negatives = s.size();
    }
    if (s.size() - num_first_adj_negatives < k) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    // flip next K pancakes from first found plus
    for (int i = 0; i < k; ++i) {
        s[i + num_first_adj_negatives] = (s[i + num_first_adj_negatives] == '+') ? '-' : '+';
    }
    findAnswer(s, k, ++flips);
}


int main(int argc, char* argv[])
{
    int t;
    cin >> t;

    string s;
    int flips;
    unsigned int k;
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;
        cout << "Case #" << i << ": ";
        flips = 0;
        findAnswer(s, k, flips);
    }

    return 0;
}
