#include <algorithm>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <set>
#include <map>
#include <memory>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <cassert>
#include <fstream>

using namespace std;

using LL = long long;


int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(24);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        string s;
        cin >> s;
        set < LL, greater < LL > > nums;
        for (int i = 0; i < s.size(); ++i) {
            if (i > 0 && s[i] < s[i - 1]) {
                break;
            }
            if (i + 1 == s.size()) {
                nums.insert(stoll(s));
                break;
            }
            auto temp = s;
            temp[i]--;
            for (int j = i + 1; j < s.size(); ++j){
                temp[j] = '9';
            }
            if (i == 0 || temp[i] >= temp[i - 1]) {
                nums.insert(stoll(temp));
            }
        }
        cout << "Case #" << tt + 1 << ": " << *nums.begin() << "\n";
    }
    return 0;
}