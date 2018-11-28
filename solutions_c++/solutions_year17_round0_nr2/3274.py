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
ll N;
string s;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> s;
		N = 0;
		for(int i=0; i<s.length(); i++) {
			N = N * (ll)(10);
			N = N + (ll)(s[i]-'0');	
		}
		if(N < 10) {
			printf("Case #%d: %lld\n", t, N);
			continue;
		}
		else {
			int lst = 0;
			bool f = 1;
			while(f) {
				f = 0;
				lst = 0;
				for(int i=0; i<s.length(); i++) {
					int x = s[i]-'0';
					if(x < lst) {
						s[i-1]--;
						for(int j=i; j<s.length(); j++) s[j] = '9';
						f = 1;
						break;
					}
					lst = x;
				}
			}
			N = 0;
			for(int i=0; i<s.length(); i++) {
				N = N * (ll)(10);
				N = N + (ll)(s[i]-'0');		
			}
			printf("Case #%d: %lld\n", t, N);
		}
	}
   
}
