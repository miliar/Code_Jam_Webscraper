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

void flip (char &c) {
    if (c == '+') c = '-';
    else c = '+';
}

int main() {
#ifdef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
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
        string S;
        int K;
        cin >> S >> K;
        int moves = 0;

        int i = 0;
        while (i != S.length()-K) {
            while (i != S.length()-K && S[i] == '+') {
                i++;
            }

            if (i == S.length()-K) break;

            for (int j = 0; j < K; j++) {
                flip(S[i+j]);
            }
            moves++;
        }

        bool allHappy = true;
        bool allBlank = true;
        while (i < S.length()) {
            if (S[i] == '-') allHappy = false;
            else if (S[i] == '+') allBlank = false;
            i++;
        }

        printf("Case #%d: ", t);
        if (!allBlank && !allHappy) {
            cout << "IMPOSSIBLE" << endl;
        } else if (allBlank) {
            cout << moves + 1 << endl;
        } else {
            cout << moves << endl;
        }
    }

    return 0;
}