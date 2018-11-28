#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL, double> PII;
typedef set<int>::iterator SIT; 

const int maxn = 1005;

int R, O, Y, G, B, V;
int bl, br, rl, rr, yl, yr;
int b, r, y, n;
vector<char> ans;

void gen(){
	int X = min(b, min(r, y));
	int Z = max(b, max(r, y));
	int W = b + r + y - Z - X;
	ans.clear();
	int tot = X + W + Z;
	for(int i = 0; i < Z; ++i){
		ans.push_back('3');
		if(i < X) ans.push_back('1');
		if(i < X + W - Z) ans.push_back('2'); 
		if(i >= X) ans.push_back('2');
	}
	char c1, c2, c3;
	if(X == b){
		c1 = 'B';
		if(W == r){
			c2 = 'R';
			c3 = 'Y';
		}
		else {
			c2 = 'Y';
			c3 = 'R';
		}
	}
	else if(X == r){
		c1 = 'R';
		if(W == b){
			c2 = 'B';
			c3 = 'Y';
		}
		else{
			c2 = 'Y';
			c3 = 'B';
		}
	}
	else{
		c1 = 'Y';
		if(W == b){
			c2 = 'B';
			c3 = 'R'; 
		}
		else{
			c2 = 'R';
			c3 = 'B';
		}
	}
	for(int i = 0; i < ans.size(); ++i){
		if(ans[i] == '1') ans[i] = c1;
		else if(ans[i] == '2') ans[i] = c2;
		else ans[i] = c3;
	}
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ", ++cases);
		if(O == B && O != 0){
			if(O + B == n){
				for(int i = 0; i < n; ++i){
					putchar((i & 1) ? 'O' : 'B');
				}
				putchar('\n');
			}
			else{
				puts("IMPOSSIBLE");
			}
			continue;
		}
		if(R == G && R != 0){
			if(R + G == n){
				for(int i = 0; i < n; ++i){
					putchar((i & 1) ? 'R' : 'G');
				}
				putchar('\n');
			}
			else{
				puts("IMPOSSIBLE");
			}
			continue;
		}
		if(Y == V && Y != 0){
			//puts("fuck");
			if(Y + V == n){
				for(int i = 0; i < n; ++i){
					putchar((i & 1) ? 'Y' : 'V');
				}
				putchar('\n');
			}
			else{
				puts("IMPOSSIBLE");
			}
			continue;
		}
		if(O > B || G > R || V > Y){
			puts("IMPOSSIBLE");
			continue;
		}
		b = B - O;
		r = R - G;
		y = Y - V;
		//printf("%d %d %d\n", b, r, y);
		if(!(b + r >= y && b + y >= r && y + r >= b)){
			puts("IMPOSSIBLE");
			continue;
		}
		gen();
		int flag = 0;
		int cnt = 0;
		for(int i = 0; i < ans.size(); ++i){
			if(ans[i] == 'B' && !(flag & 4)){
				for(int i = 0; i < O; ++i){
					putchar('B');
					putchar('O');
					cnt += 2;
				}
				flag |= 4;
			} 
			if(ans[i] == 'R' && !(flag & 2)){
				for(int i = 0; i < G; ++i){
					putchar('R');
					putchar('G');
					cnt += 2;
				}
				flag |= 2;
			}
			if(ans[i] == 'Y' && !(flag & 1)){
				for(int i = 0; i < V; ++i){
					putchar('Y');
					putchar('V');
					cnt += 2;
				}
				flag |= 1;
			}
			putchar(ans[i]);
			cnt++;
		}
		assert(cnt == n);
		puts("");
	}
	return 0;
}
