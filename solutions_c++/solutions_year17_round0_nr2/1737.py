#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve (ll tc) {
	char x[25], cur = '9';
	scanf("%s",x);
	printf("Case #%lld: ",tc);
	ll n = strlen(x), f1 = 0;
	for(int i=0;i<n;i++) {
		if(x[i] == '0') {
			if(f1 == 0) {
				for(int j=0;j<n-1;j++) putchar('9');
				puts("");
				return;
			}
			x[f1-1]--;
			for(int j=f1;j<n;j++) x[j] = '9';
		}
		else if(x[i] != '1') f1 = i+1;
	}
	for(int i=n;i--;) {
		if(x[i] > cur) {
			for(int j=i+1;j<n;j++) x[j] = '9';
			x[i]--;
		}
		cur = x[i];
	}
	printf("%s\n",x);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll tc;
	scanf("%lld",&tc);
	for(ll i=1;i<=tc;i++) solve(i);
}
