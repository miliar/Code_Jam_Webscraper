#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#define LL long long
#define N 55
#define M 2600
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
using namespace std;

int t, n, m, rat[N], s[N][N], l[N][N], r[N][N], ptr[N], val[M], cv;

void solve(int tc){
	cv = 0;
	scanf("%d %d", &n, &m);
	fi(i, 0, n) scanf("%d", &rat[i]);
	fi(i, 0, n){
		fi(j, 0, m) scanf("%d", &s[i][j]);
		sort(s[i], s[i] + m);
		fi(j, 0, m){
			if(s[i][j] * 10 % (11 * rat[i]) == 0) l[i][j] = s[i][j] * 10 / 11 / rat[i];
			else l[i][j] = s[i][j] * 10 / (11 * rat[i]) + 1;
			r[i][j] = s[i][j] * 10 / (9 * rat[i]);
			val[cv++] = l[i][j];
		}
		ptr[i] = 0;
	}
	
	sort(val, val + cv);
	cv = unique(val, val + cv) - val;
	
	int ans = 0;
	bool fail = 0;
	fi(v, 0, cv){
		fi(i, 0, n){
			while(ptr[i] < m && r[i][ptr[i]] < val[v]) ptr[i]++;
			if(ptr[i] == m){
				fail = 1;
				break;
			}
		}
		if(fail) break;
		bool ok = 1;
		while(ok && !fail){
			fi(i, 0, n) if(!(l[i][ptr[i]] <= val[v] && r[i][ptr[i]] >= val[v])) ok = 0;
			if(ok){
				ans++;
				fi(i, 0, n){
					ptr[i]++;
					if(ptr[i] == m) fail = 1;
				}
			}
		}
	}
	
	printf("Case #%d: %d\n", tc, ans);
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

