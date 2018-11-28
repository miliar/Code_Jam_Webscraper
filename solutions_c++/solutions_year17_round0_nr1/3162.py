
/******************** Beginning of Template **************************/
/************ ALL HEADER FILE ***********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <utility>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <cassert>

using namespace std;

/************* ALL DEFINE ***************/
#define MEM(a, b) memset(a, b, sizeof a);
#define FORS(i, j, k, step) for (int i=j; i<k; i+=step)
#define FOR(i, j, k) for (int i=j; i<k; i++)
#define RFORS(i, j, k, step) for (int i=j; i>=k; i-=step)
#define RFOR(i, j, k, step) for(int i=j; i>=k; i--)
#define REP(i, k) for(int i = (0); i < (k); i++ )
#define RREP(i, k) for(int i = j; i >= (k); i-- )

#define ALL(cont) cont.begin(), cont.end()
#define RALL(cont) cont.begin(), cont.end()
#define FOREACH(it, l) for(auto it=l.begin(); it != l.end(); it++)
#define mp make_pair
#define pb push_back
#define debug puts("Fango")
#define INF (int)MAX_INT
#define EPS (int)1e-9
#define PI acos(-1)
#define MOD 1000000007

/****************** TYPEDEF *****************/
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vii;
typedef vector<piii> viii;
typedef long long int32;
typedef unsigned long long uint32;
typedef long long int int64;
typedef unsigned long long int uint64;

template <class T>
    T sqr(T val) {
        return val * val;
    }


/*********************** End of Template **************************/

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int TC;
    cin >> TC;
    REP(tc, TC) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        REP(i, s.size() - k + 1) {
            if (s[i] == '-') {
                ans++;
                REP(j, k) {
                    if (s[j + i] == '+') s[j + i] = '-';
                    else s[j + i] = '+';
                }
                //cout << s.c_str() << endl;
            }
        }

        REP(i, s.size()) if (s[i] == '-') {
                ans = -1;break;
            }
        cout << "Case #" << tc + 1 << ": " << (ans == -1 ? "IMPOSSIBLE" : to_string(ans))<< endl;
    }
}


