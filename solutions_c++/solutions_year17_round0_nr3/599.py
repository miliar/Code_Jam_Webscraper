#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#define LL long long
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
using namespace std;

int t;
char s[1005];

void solve(int tc){
	printf("Case #%d: ", tc);
	LL x, y;
	scanf("%I64d %I64d", &x, &y);
	
	LL c1 = 1, c0 = 0;
	while(true){
		if(y <= c1){
			printf("%I64d %I64d\n", x / 2, (x - 1) / 2);
			return;
		}
		y -= c1;
		if(y <= c0){
			printf("%I64d %I64d\n", (x - 1) / 2, (x - 2) / 2);
			return;
		}
		y -= c0;
		
		if(x % 2) c1 = c1 * 2 + c0;
		else c0 = c0 * 2 + c1;
		
		x /= 2;
	}
}

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

