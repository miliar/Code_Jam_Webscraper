#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 60;
const int P = 1e9+7;

int a[MAXN][MAXN];
int b[MAXN];
pair<int, int> p[MAXN][MAXN];

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, m;
		int i, j, k;
		scanf("%d%d", &n, &m);
		for(i = 0; i < n; i++)
			scanf("%d", &b[i]);
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++){
				scanf("%d", &a[i][j]);
				int l, r;
				l = (a[i][j]*10-1) / (b[i]*11) + 1;
				r = (a[i][j]*10) / (b[i]*9);
				if(l <= r)
					p[i][j] = mp(l, r);
				else
					p[i][j] = mp(-1, -1);
			}
		for(i = 0; i < n; i++){
			sort(p[i], p[i]+m);
//			for(j = 0; j < m; j++)
//				printf("%d %d\n", p[i][j].fi, p[i][j].se);
			for(b[i] = 0; b[i] < m; b[i]++)
				if(p[i][b[i]].fi != -1)
					break;
		}
		int ans = 0;
		while(true){
			int lo, hi;
			lo = 1;
			hi = 1e9;
			for(i = 0; i < n; i++){
				if(b[i] == m)
					break;
				lo = max(lo, p[i][b[i]].fi);
				hi = min(hi, p[i][b[i]].se);
			}
			if(i < n)
				break;
			//printf("%d %d\n", lo, hi);
			if(lo <= hi){
				ans++;
				for(i = 0; i < n; i++)
					b[i]++;
			}
			else{
				for(i = 0; i < n; i++)
					if(p[i][b[i]].se < lo)
						b[i]++;
			}
		}
		printf("Case #%d: %d\n", i0, ans);
	}
	return 0;
}
