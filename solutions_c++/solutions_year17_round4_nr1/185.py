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
const int MAXN = 110;
const int P = 1e9+7;

int f[MAXN][MAXN][MAXN];
int a[MAXN];

void up(int i, int j, int k, int x, int y, int z){
	f[i+x][j+y][k+z] = max(f[i+x][j+y][k+z], f[i][j][k]+1);
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	memset(f, 0, sizeof f);
	int i, j, k;
	f[0][0][1] = f[0][1][0] = f[1][0][0] = 1;
	for(i = 0; i <= 100; i++)
		for(j = 0; j <= 100; j++)
			for(k = 0; k <= 100; k++){
				f[i+1][j][k] = max(f[i+1][j][k], f[i][j][k]);
				f[i][j+1][k] = max(f[i][j+1][k], f[i][j][k]);
				f[i][j][k+1] = max(f[i][j][k+1], f[i][j][k]);
				up(i, j, k, 4, 0, 0);
				up(i, j, k, 0, 2, 0);
				up(i, j, k, 0, 0, 4);
				up(i, j, k, 1, 0, 1);
				up(i, j, k, 2, 1, 0);
				up(i, j, k, 0, 1, 2);
			}
	for(i0 = 1; i0 <= T; i0++){
		int n, p;
		int ans = 0;
		scanf("%d%d", &n, &p);
		memset(a, 0, sizeof a);
		for(i = 0; i < n; i++){
			int t;
			scanf("%d", &t);
			t %= p;
			a[t]++;
		}
		if(p == 2){
			ans = a[0] + (a[1]+1) / 2;
		}
		if(p == 3){
			int x = min(a[1], a[2]);
			ans = a[0] + x + (a[1]-x+2)/3 + (a[2]-x+2)/3;
		}
		if(p == 4){
			ans = a[0] + f[a[1]][a[2]][a[3]];
		}
		printf("Case #%d: %d\n", i0, ans);
	}
	return 0;
}
