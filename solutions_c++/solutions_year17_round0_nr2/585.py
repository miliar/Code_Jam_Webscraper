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
	scanf("%s", s);
	int n = strlen(s);
	
	for(int i = n - 2; i >= 0; i--){
		if(s[i] > s[i + 1]){
			s[i] = s[i] - 1;
			fi(j, i + 1, n) s[j] = '9';
		}
	}
	
	if(s[0] == '0'){
		fi(i, 0, n - 1) s[i] = s[i + 1];
		s[--n] = 0;
	}
	printf("Case #%d: %s\n", tc, s);
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}

