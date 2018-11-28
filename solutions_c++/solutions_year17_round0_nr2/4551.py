#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <stack>
#include <list>
#include <forward_list>
#include <algorithm> // max...
#include <utility> // pair
#include <complex>
#include <climits> // int, ll...
#include <limits> // double...
#include <cmath> // abs, atan...
#include <cstring> // memset
#include <string>
#include <functional> // greater, less...
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, double> id;
typedef pair<double, int> di;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef vector<id> vid;
typedef vector<vi> vvi;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, ll> mll;

#define ONLINE_JUDGE

void down(char &c) {
    if (c == '0') c = '9';
    else c = char(c - 1);
}

void tidy(string &s) {
    for (int i = 0; i < s.length()-1; i++) {
        if (s[i] > s[i+1]) {
            down(s[i]);
            for (int j = i+1; j < s.length(); j++)
                s[j] = '9';
            tidy(s);
            if (s[0] == '0') s.erase(0, 1);
            return;
        }
    }
}

int main() {
#ifdef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
        freopen("B-large.out", "w", stdout);
        //freopen("X-large-practice.in", "r", stdin);
        //freopen("X-large-practice.out", "w", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
#endif
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;

        printf("Case #%d: ", t);

        tidy(s);
        cout << s << endl;
    }

    return 0;
}