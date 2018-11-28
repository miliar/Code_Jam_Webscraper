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
    ifstream cin("/Users/shicheng/Downloads/B-large.in.txt");
    ofstream cout("/Users/shicheng/Downloads/B-large.out.txt");
    int t;
    cin >> t;
    for (int num = 0; num < t; ++num) {
        string s;
        cin >> s;
        for (string::size_type i = s.size() - 1; i >= 1; --i) {
            if (s[i] == '0' || s[i] < s[i - 1]) {
                --s[i - 1];
                for (string::size_type j = i; j < s.size(); ++j) {
                    if (s[j] == '9') {
                        break;
                    }
                    s[j] = '9';
                }
            }
        }
        string::size_type pos_0 = s.rfind('0');
        if (pos_0 != string::npos) {
            s = s.substr(pos_0 + 1);
        }
        cout << "Case #" << num + 1 << ": " << s << endl;
    }
}
