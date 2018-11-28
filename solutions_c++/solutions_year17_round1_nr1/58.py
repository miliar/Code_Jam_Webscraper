#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#define LL long long
#define N 31
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
using namespace std;

int t, n, m;
char s[N][N];

void solve(int tc){
	printf("Case #%d:\n", tc);
	scanf("%d %d", &n, &m);
	fi(i, 0, n) scanf("%s", s[i]);
	
	bool ft = 0;
	fi(i, 0, n){
		int f = -1;
		fi(j, 0, m) if(s[i][j] != '?'){
			f = j;
			break;
		}
		if(f >= 0){
			FD(j, f - 1, 0) s[i][j] = s[i][j + 1];
			fi(j, f + 1, m) if(s[i][j] == '?') s[i][j] = s[i][j - 1];
			if(!ft) FD(j, i - 1, 0) fi(k, 0, m) s[j][k] = s[j + 1][k];
			ft = 1;
		}else if(ft){
			fi(j, 0, m) s[i][j] = s[i - 1][j];
		}
	}
	
	fi(i, 0, n) puts(s[i]);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

