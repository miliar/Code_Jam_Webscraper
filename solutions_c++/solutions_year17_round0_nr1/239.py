// Compile with MinGW-64 (6.3.0) in MSYS2

#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    std::vector<bool> pancakes;
    while (true) {
        char c;
        cin.get(c);
        if (c == '+')
            pancakes.push_back(true);
        else if (c == '-')
            pancakes.push_back(false);
        else if (c == ' ')
            break;
        else {
            cerr << "Error!!!";
            break;
        }
    }

    int k;
    cin >> k;

    string s;
    getline(cin, s);

    int l = pancakes.size();
    int numFlips = 0;
    for (int i=0; i<l; i++) {
        if (!pancakes[i]) {
            if (l-i >= k) {
                for (int j=i; j<i+k; j++) {
                    pancakes[j] = !pancakes[j];
                }
                numFlips++;
            } else {
                cout << "IMPOSSIBLE" << "\n";
                return;
            }
        }
    }
    
    cout << numFlips << "\n";
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for(int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}