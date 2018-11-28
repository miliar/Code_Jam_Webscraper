#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define what_is(x) cerr << #x << " is " << x << endl

ll reachCounter = 0;
#define Reached cout<<"Reached here with Counter #"<<reachCounter<<"\n", reachCounter++;

#define N 200005

#define newLine	printf("\n");

#define sll(X) scanf("%lld", &X);
#define pll(X) printf("%lld", X);
#define printAll(X, n)	for(int i=0;i<n;i++)	printf("%lld ", X[i]); newLine;
#define scanAll(X, n)	for(int i=0;i<n;i++)	scanf("%lld", &X[i]);

string s;

int main() {
	freopen("inB", "r", stdin);
	freopen("outB", "w", stdout);
	ll t;
	sll(t);
	for(int cases = 1; cases <= t; cases ++) {
		cin>>s;
		cout<<"Case #"<<cases<<": ";
		if(s.size() == 1) {
			cout<<s<<"\n";
			continue;
		}
		ll ind = -1;
		for(int i=1;i<s.size();i++) {
			if(s[i] >= s[i-1]) {
				;
			} else {
				ind = i - 1;
				break;
			}
		}
		if(ind == -1) {
			cout<<s<<"\n";
			continue;
		}
		while(ind > 0 && s[ind] - '0' - 1 < s[ind-1] -'0') {
			ind --;
		}
		string ans;
		if(ind) {
			for(int i=0;i<ind;i++) {
				ans += s[i];
			}
			ans += s[ind]-1;
			for(int i=ind+1;i<s.size();i++) {
				ans += '9';
			}
		} else {
			if(s[0] != '1') {
				ans += s[0] - 1;
			}
			for(int i=0;i<s.size()-1;i++) {
				ans += '9';
			}
		}
		cout<<ans<<"\n";
	}
	return 0;
}