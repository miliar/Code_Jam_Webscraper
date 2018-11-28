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

int64 pangkat(int64 t) {
    int64 sum = 0, ctr = 1;
    while (ctr != t){
        sum += ctr;
        ctr *= 2;
    }
    if (sum == 0) sum = 1;
    return sum;
}
int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int TC;
    cin >> TC;
    REP(tc, TC) {
        int64 x, n;

        cin >> x >> n;
        int64 ganjil = (x % 2 == 1 ? x : 0);
        int64 genap = (x % 2 == 0? x : 0);
        int64 ganjil_n = (ganjil == 0 ? 0: 1);
        int64 genap_n = (genap == 0 ? 0 : 1);

        int64 time = 1;
        while (n >= time*2) {
            int64 a_n = 0, b_n = 0;
            int64 a = ganjil == 0 ? 0 : ganjil -1;
            int64 b = genap == 0 ? 0 : genap - 1;

            if ((a / 2) % 2 == 0) a_n += ganjil_n * 2;
            else b_n += ganjil_n * 2;

            a_n += genap_n; b_n += genap_n;
            if ((b / 2) % 2 == 0) {
                genap = b / 2, ganjil = b - b/2;
            }
            else {
                genap = b - b/2, ganjil = b/2;
            }
            if ((b == 0)) {
                if ((a / 2) % 2 ==0) genap = a / 2;
                else ganjil = a /2;
            }
            genap_n = a_n; ganjil_n = b_n;
/*            cout << ganjil << " " << ganjil_n << endl;
        cout << genap << " " << genap_n << endl;
        cout << "-----------\n";*/
        time*=2;
        }
        /*cout << ganjil << " " << ganjil_n << endl;
        cout << genap << " " << genap_n << endl;
        cout << "-----------\n";*/

        pair<int64, int64> big, small;
        if (ganjil > genap) big = mp(ganjil - 1, ganjil_n), small = mp(genap - 1, genap_n);
        else big = mp(genap - 1, genap_n), small = mp(ganjil - 1, ganjil_n);

        time = pangkat(time);
        int64 ke = n - time;
        cout << "Case #" << tc + 1 << ": ";
        if (ke <= big.second) cout << max(big.first /2, big.first-big.first/2)<< " " << min(big.first /2, big.first-big.first/2);
        else cout << max(small.first /2, small.first-small.first/2)<< " " << min(small.first /2, small.first-small.first/2);
        cout << endl;

    }
}
