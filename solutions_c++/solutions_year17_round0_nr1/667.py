#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		string s;
		int k;
		cin >> s >> k;
		//cout << s << k << endl;
		int ans = 0;
		for(int i = 0; i + k <= s.size(); i++) {
			if(s[i] == '-') {
				for(int j = i; j< i + k; j++) {
					s[j] = (s[j]=='+'?'-':'+');
				}
				ans++;
			}
		}
		bool f = true;
		for(int i = 0; i < s.size(); i++) {
			if(s[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", Case);
				f = false;
				break;
			}
		}
		if(f) printf("Case #%d: %d\n", Case, ans);
		//cout << s << endl;
	}
}