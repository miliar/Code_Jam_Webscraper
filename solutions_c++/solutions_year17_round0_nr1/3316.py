#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
#define MAXN 1005
#define MAXM 1005
#define MAXP 25
#define INF 2000000000
#define HAX 10000000 
#define A first
#define B second
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define re(i, n) FOR(i, 1, n)
#define rep(i, n) for(int i = 0; i<(n); ++i)
#define fore(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
int N, K;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		string s;
		cin >> s;
		N = (int)s.length();
		cin >> K;
		int ans = 0;
		string tmp = s;
		for(int i=0; i+K-1<N; i++) {
			if(tmp[i] == '+') continue;
			ans++;
			for(int j=i; j<=i+K-1; j++) {
				if(tmp[j] == '+') tmp[j] = '-';
				else tmp[j] = '+';
			}
		}
		bool f = 0;
		for(int i=0; i<N; i++) if(tmp[i] != '+') f = 1;
		if(f == 0) {
			printf("Case #%d: %d\n", t, ans);
		}
		
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
   
}
