#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <unordered_map>
#include <string.h>
#include <bitset>

#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define ll long long
#define forn(i, n) for (int i = 0; i < (int) (n); i++)
#define forlr(i, l, r) for (int i = (int) l; i <= (int) (r); i++)
#define forrl(i, r, l) for (int i = (int) r; i >= (int) (l); i--)

using namespace std;

ll const MOD = 1000000007;
ll const LLINF = 1000000000000000000;
int const INF = 1000000000;

int const MAXN = 1000000;


int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);

    int t;
    cin >> t;

    forn(cur_t, t) {
        int n, k;
        cin >> n >> k;
        multiset<int> s;
        s.insert(n);
        forn(i, k - 1) {
        	auto it = --s.end();
        	int x = *it;
        	s.erase(it);
        	s.insert((x - 1) / 2);
        	s.insert(x - 1 - (x - 1) / 2);
        }

		auto it = --s.end();
        int x = *it;
        cout << "Case #" << cur_t + 1 << ": " << x - 1 - (x - 1) / 2 << " " << (x - 1) / 2 << "\n";
    }
    
    

    return 0;
}









