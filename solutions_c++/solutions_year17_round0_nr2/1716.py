#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<set>
#include<sstream>
#include<complex>
using namespace std;
string s;
void getinput() {
    cin >> s;
}
void process() {
    vector<int> minRight = vector<int>(s.size(), 11);
    for(int i = s.size() - 1; i >= 0; --i) {
        minRight[i] = s[i] - '0';
        if (i < s.size() - 1) minRight[i] = min(minRight[i + 1], minRight[i]);
    }
    string res = s;
    for(int i = 0; i < s.size() - 1; i ++) {
        if (s[i] > s[i + 1]) {
            int j = i;
            while (j > 0 && s[j] <= s[j - 1]) --j;
            res = "";
            for(int k = 0; k < j; k ++) res += s[k];
            res += s[j] - 1;
            for(int k = j + 1; k < s.size(); k ++) res += "9";
            while (res[0] == '0') res = res.substr(1, res.size() - 1);
            break;
        }
    }
    cout << res << endl;
}
int main() {
//    freopen("D:\\Projects\\GGCodeJam\\bai1.inp", "r", stdin);
//    freopen("D:\\Projects\\GGCodeJam\\bai1.out", "w", stdout);
    int t; cin >> t;
    for(int test = 0; test < t; test ++) {
        getinput();
        cout << "Case #" << test + 1 << ": ";
        process();
    }
    return 0;
}
