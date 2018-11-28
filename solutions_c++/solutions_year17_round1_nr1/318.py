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

char A[30][30];

void Do(int a, int b, int c, int d){
	int chk[30] = {};
	for(int i=a;i<=b;i++)for(int j=c;j<=d;j++)if(A[i][j] != '?')chk[A[i][j]-'A'] = 1;
	int cnt = 0;
	rep(i,26)cnt += chk[i];
	if(cnt == 1){
		int t = (int)(max_element(chk, chk+26) - chk);
		for(int i=a;i<=b;i++)for(int j=c;j<=d;j++)A[i][j] = 'A' + t;
		return;
	}
	for(int i=a;i<b;i++){
		memset(chk, 0, sizeof chk);
		int ok = 1, ok2 = 1, ok3 = 1;
		for(int x=a;x<=i;x++)for(int j=c;j<=d;j++)if(A[x][j] != '?')chk[A[x][j] - 'A'] = 1, ok2 = 0;
		for(int x=i+1;x<=b;x++)for(int j=c;j<=d;j++)if(A[x][j] != '?'){ok3 = 0; if(chk[A[x][j] - 'A'])ok = 0; }
		if(ok && !ok2 && !ok3){
			Do(a, i, c, d);
			Do(i+1, b, c, d);
			return;
		}
	}
	for(int i=c;i<d;i++){
		memset(chk, 0, sizeof chk);
		int ok = 1, ok2 = 1, ok3 = 1;
		for(int x=a;x<=b;x++)for(int j=c;j<=i;j++)if(A[x][j] != '?')chk[A[x][j] - 'A'] = 1, ok2 = 0;
		for(int x=a;x<=b;x++)for(int j=i+1;j<=d;j++)if(A[x][j] != '?'){ok3 = 0; if(chk[A[x][j] - 'A'])ok = 0; }
		if(ok && !ok2 && !ok3){
			Do(a, b, c, i);
			Do(a, b, i+1, d);
			return;
		}
	}
}

void solve(){
	int n, m; scanf("%d%d", &n, &m);
	rep(i, n)scanf("%s", A[i]);
	Do(0, n-1, 0, m-1);
	rep(i, n)printf("%s\n", A[i]);
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d:\n", tc);
		solve();
	}
	return 0;
}
