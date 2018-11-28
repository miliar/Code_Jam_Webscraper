#include <iostream>
#include <map>
#include <iterator>
#include <queue>
#include <set>
#include <stack>
#include <iomanip>
#include <math.h>
#include <unordered_map>
#include <sstream>
#include <fstream>

using namespace std;

int main() {
    ifstream cin("/Users/shicheng/Downloads/A-large.in.txt");
    ofstream cout("/Users/shicheng/Downloads/A-large.out.txt");
    int t;
    cin >> t;
    for (int num = 0; num < t; ++num) {
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        for (string::size_type i = 0; i <= s.size() - k; ++i) {
            if (s[i] == '-') {
                ++cnt;
                for (int j = 0; j < k; ++j) {
                    if (s[i + j] == '-') {
                        s[i + j] = '+';
                    }
                    else {
                        s[i + j] = '-';
                    }
                }
            }
        }
        bool possible = true;
        for (string::size_type i = s.size() - k + 1; i < s.size(); ++i) {
            if (s[i] == '-') {
                possible = false;
                break;
            }
        }
        if (possible) {
            cout << "Case #" << num + 1 << ": " << cnt << endl;
        }
        else {
            cout << "Case #" << num + 1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
}
