#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <bitset>

using namespace std;
typedef pair<int, int> Pi;
typedef long long ll;
#define pii Pi
#define pll PL
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> PL;
typedef long double ldouble;

void solve(){
	string S; int K; cin >> S >> K;
	int n = sz(S);
	int ans = 0;
	for(int i=0;i<=n-K;i++){
		if(S[i] == '-'){
			rep(j, K)S[i+j] = (S[i+j] == '-' ? '+' : '-');
			++ans;
		}
	}
	rep(i, n)if(S[i] == '-'){
		puts("IMPOSSIBLE");
		return;
	}
	printf("%d\n", ans);
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
}
