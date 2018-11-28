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

ll n, k;
string s;

int main() {
	freopen("inA", "r", stdin);
	freopen("outA", "w", stdout);
	ll t;
	sll(t);
	for(int cases = 1; cases <= t; cases ++) {
		cin>>s;
		n = s.size();
		sll(k);
		cout<<"Case #"<<cases<<": ";
		ll ans = 0;
		bool flag = 0;
		for(int i=0;i<n;i++) {
			if(s[i] == '-') {
				if(i+k > n) {
					flag = 1;	
				}
				for(int j=0;j<k && i+j<n;j++) {
					if(s[i+j] == '-') {
						s[i+j] = '+';
					} else {
						if(i+k == n) {
							flag = 1;
						}
						s[i+j] = '-';
					}
				}
				ans ++;
			}
		}
		if(flag) {
			cout<<"IMPOSSIBLE";
		} else {
			cout<<ans;
		}
		newLine
	}
	return 0;
}