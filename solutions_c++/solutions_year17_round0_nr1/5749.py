#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define eps 1e-9
#define all(a)   a.begin(),a.end()
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define sz size()
#define rd(inp) scanf("%lld",&inp)
#define rd2(inp1, inp2) scanf("%lld %lld",&inp1, &inp2)
#define rl(inp) scanf("%d",&inp)
#define pf(out) printf("%lld\n", out);

const long long linf = 1e18+5;
const int mod = (int) 1e9 + 7;
const int inf = 1e9;

ll read(){
	bool minus = false;
	ll result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus){
		return -result;
	}
	else{
		return result;
	}
}

ll fpow(ll base,ll power){
	ll result = 1;
	while (power > 0){
		if (power%2 == 1) result=(result*base);
  		base = (base*base);
  		power /= 2;
  	}
	return result;
}

void solve(){
	string str;
	cin >> str;
	int k, i, j, ans = 0;
	cin >> k;
	for ( i = 0 ; i + k - 1 < str.sz ; i ++ ){
		if ( str[i] == '-' ){
			j = i;
			ans ++;
			int cnt = 0;
			while ( cnt < k && j < str.sz ){
				if ( str[j] == '-' ){
					str[j] = '+';
				}
				else{
					str[j] = '-';
				}
				j ++;
				cnt ++;
			}
		}
	}
	for ( i = 0 ; i < str.sz ; i ++ ){
		if ( str[i] == '-' ){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", ans);
	return;
}

int main(){
	int t, i = 1;
	cin >> t;
	while( t-- ){
		printf("Case #%d: ", i++);
		solve();
	}
	return 0;
}