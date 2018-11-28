#include <cstdio>
#include <algorithm>
#include <queue>
#define LL long long
#define N 4
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
using namespace std;

int t, n, p, c[N];

void solve(int tt){
	printf("Case #%d: ", tt);
	
	scanf("%d %d", &n, &p);
	
	int ans = 0;
	fi(i, 0, 4) c[i] = 0;
	fi(i, 0, n){
		int x;
		scanf("%d", &x);
		c[x % p]++;
	}
	
	if(c[0] == n){
		printf("%d\n", n);
		return;
	}
	
	fi(i, 1, 4) if(c[i]){
		c[i]--;
		if(p <= 3){
			int lim = min(c[1], c[2]);
			ans = max(ans, c[0] + 1 + lim + (c[1] - lim) / p + (c[2] - lim) / p);
		}else{
			int lim = min(c[1], c[3]);
			int r1 = c[1] - lim;
			int r3 = c[3] - lim;
			int ret = c[0] + 1 + lim + c[2] / 2;
			if(c[2] % 2){
				if(r1 >= 2) ret++, r1 -= 2;
				else if(r3 >= 2) ret++, r3 -= 2;
			}
			ret += r1 / 4 + r3 / 4;
			ans = max(ans, ret);
		}
		c[i]++;
	}
	printf("%d\n", ans);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

