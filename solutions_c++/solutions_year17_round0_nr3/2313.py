#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

pll new_gap_sizes(ll gap_size){
    if (gap_size % 2LL == 1)
        return mp(gap_size / 2, gap_size / 2);
    else
        return mp(gap_size / 2, gap_size / 2 - 1);
}

void insert_new_gaps(set<pll> &S, ll gap_size, ll gap_count){
    ll new_gap_count = gap_count;
    set<pll>::iterator a = S.lower_bound(mp(gap_size, 1));
    
    if (a != S.end() && (*a).ff == gap_size){
        new_gap_count += (*a).ss;
        S.erase(a);
    }

    S.insert(mp(gap_size, new_gap_count));
}

void solve(){
    ll n, k;
    scanf(" %Ld %Ld", &n, &k);

    set<pll> S;
    S.insert(mp(n, 1));

    while(k > 0){
        set<pll>::iterator x = S.end(); --x;
        ll gap_size = (*x).first;
        ll gap_count = (*x).second;
        // printf("%Ld %Ld\n", gap_size, gap_count);
        S.erase(x);
        
        pll ngs = new_gap_sizes(gap_size);
        
        if (gap_count >= k){
            printf("%Ld %Ld\n", ngs.ff, ngs.ss);
            return;
        }

        k -= gap_count;
        insert_new_gaps(S, ngs.ff, gap_count);
        insert_new_gaps(S, ngs.ss, gap_count);
    }

}

int main(){
  int T;
  scanf(" %d", &T);
  For(t,T){
    printf("Case #%d: ",t+1);
    solve();
  }
  return 0;
}