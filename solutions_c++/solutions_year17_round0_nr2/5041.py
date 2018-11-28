#include <bits/stdc++.h>
using namespace std;

const int N = 22;

int n;
char s[N];
int vis[N][10][2][2];
string dp[N][10][2][2];

string solve(int pos = 0, int last = 0, bool equal = true, bool zero = true){
	if(pos == n) return "";
	string &ret = dp[pos][last][equal][zero];
	if(!vis[pos][last][equal][zero]){
		vis[pos][last][equal][zero] = true;
		int start = equal? s[pos] - '0' : 9;
		for(int i = start; i >= last; i--){
			bool nequal = equal && (i == s[pos] - '0'), nzero = zero && (i == 0);
			string go = solve(pos + 1, i, nequal, nzero);
			if((int)go.size() == n - pos - 1){
				char c = i + '0';
				if(!nzero) go = c + go;
				return go;
			}
		}
	}
	return ret;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k++){
		scanf("%s", s);
		n = strlen(s);
		memset(vis, 0, sizeof(vis));
		printf("Case #%d: %s\n", k, solve().c_str());
	}
	return 0;
}
