#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

int n, r, o, y, g, b, v;
char s[2000];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("x.out", "w", stdout);

	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", ++ca);
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		if(o > b || g > r || v > y){
			printf("IMPOSSIBLE\n");
			continue;
		}else{
			if(o == b && o){
				if(o + b == n){
					for(int i = 1; i <= n / 2; ++i)
						putchar('O'), putchar('B');
					puts("");
				}else printf("IMPOSSIBLE\n");
			}else if(g == r && g){
				if(g + r == n){
					for(int i = 1; i <= n / 2; ++i)
						putchar('G'), putchar('R');
					puts("");
				}else printf("IMPOSSIBLE\n");
			}else if(v == y && v){
				if(v + y == n){
					for(int i = 1; i <= n / 2; ++i)
						putchar('V'), putchar('Y');
					puts("");
				}else printf("IMPOSSIBLE\n");
			}else{
				b -= o, y -= v, r -= g;
				int cnt = b + y + r;
				if(max(r, max(y, b)) > cnt - max(r, max(y, b))){
					printf("IMPOSSIBLE\n");
					continue;
				}
				if(r >= y && r >= b) s[1] = 'R', r--;
				else if(y >= r && y >= b) s[1] = 'Y', y--;
				else s[1] = 'B', b--;
				for(int i = 2; i <= cnt; ++i){
					if(s[i - 1] == 'R'){
						if(y > b || y == b && s[1] == 'Y') s[i] = 'Y', y--;
						else s[i] = 'B', b--;
					}else if(s[i - 1] == 'B'){
						if(y > r || y == r && s[1] == 'Y') s[i] = 'Y', y--;
						else s[i] = 'R', r--;
					}else{
						if(r > b || r == b && s[1] == 'R') s[i] = 'R', r--;
						else s[i] = 'B', b--;
					}
				}
				assert(s[1] != s[cnt]);
				bool flagb = 0, flagr = 0, flagy = 0;
				for(int i = 1; i <= cnt; ++i){
					if(s[i] == 'R'){
						if(flagr) putchar(s[i]);
						else{
							for(int j = 1; j <= g; ++j) putchar('R'), putchar('G');
							putchar('R');
						}
						flagr = 1;
					}else if(s[i] == 'B'){
						if(flagb) putchar(s[i]);
						else{
							for(int j = 1; j <= o; ++j) putchar('B'), putchar('O');
							putchar('B');
						}
						flagb = 1;
					}else{
						if(flagy) putchar(s[i]);
						else{
							for(int j = 1; j <= v; ++j) putchar('Y'), putchar('V');
							putchar('Y');
						}
						flagy = 1;
					}
				}
				puts("");
			}
		}
	}
	return 0;
}
