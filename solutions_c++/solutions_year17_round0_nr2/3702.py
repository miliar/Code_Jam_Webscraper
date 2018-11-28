#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

bool isless(const string &s1, const string &s2) {

    if (s1.length() < s2.length()) return true;
    if (s1.length() > s2.length()) return false;

    for (int i=0; i<s1.length(); i++) {
        if (s1[i] > s2[i]) {
            return false;
        }
        else if (s1[i] < s2[i]) {
            return true;
        }
    }

    return true;
}

string solve(string s, int len) {

    string str;
    for (int i=0; i<len; i++) str += '1';

    //cout<<str<<endl;

    if (!isless(str, s)) return "";

    for (int i=0; i<len; i++) {
        int last = i==0 ? 1 : str[i-1]-'0';
        for (int j=last; j<10; j++) {
            string tmp = str;
            for (int k=i; k<len; k++) str[k] = '0' + j;
            if (!isless(str, s)) {
                str = tmp;
                break;
            }
        }
    }

    return str;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int cas=1; cas<=t; cas++) {

        string s;
        cin>>s;

        string res = solve(s, s.length());

        if (res == "") res = solve(s, s.length()-1);

        printf("Case #%d: %s\n", cas, res.c_str());

    }

    return 0;

}
