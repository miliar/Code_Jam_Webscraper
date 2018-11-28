#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <cassert>

using namespace std;

void flip(string &s, int start, int k) {
    for (int i = start; i < start + k; ++i) {
        assert(i < s.length());

        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
}
void printSolution(const string &s, int k) {
    string cake = s;
    int count = 0;
    for (int i = 0; i <= cake.length() - k; ++i) {
        if (cake[i] == '+') {
            continue;
        }
        flip(cake, i, k);
        count++;
    }
    
    if (cake.find_last_of('-') != string::npos) {
        cout << "IMPOSSIBLE";
    } else {
        cout << count;
    }
    cout << endl;
}

int main(int argc, char *argv[]) {
    clock_t tick = clock();
    int t;

    cin >> t;

    for (int i = 1; i <= t; ++i) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i << ": ";
        printSolution(s, k);
    }

    cerr << "time = " <<  clock() - tick << endl;
    return 0;
}