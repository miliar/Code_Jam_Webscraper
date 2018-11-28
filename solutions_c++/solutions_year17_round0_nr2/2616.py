
#include<bits/stdc++.h>

using namespace std;

#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define pri(x) printf("%d",x)
#define pll(x) printf("%lld",x)
#define sstr(s) scanf("%s",s)
#define nl printf("\n")
#define ll long long int
#define pii pair<int,int>
#define pLL pair<ll,ll>
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define SZ 100005
#define FOR(i,x,y) for(int i=x;i<y;i++)
#define mod 1000000007

int main()
{
    freopen("codejam17b2.in","r",stdin);
    freopen("codejam17b2.out","w",stdout);
    int t; si(t);
    int tc=1;
    while(t--) {
	string s; cin>>s;
	ll num = 0;
	ll sub;
	int flag = 1;
	while(flag) {
	    flag = 0;
	    num = sub = 0;
	    for(int i=0;i<s.length();i++) {
		num = num*10 + (s[i]-'0');
	    }
	    for(int i=1;i<s.length();i++) {
		if(s[i] < s[i-1]) {
		    flag = 1;
		    for(int j=i;j<s.length();j++) {
			sub = sub*10 + (s[j]-'0');
		    }
		    sub++;
		    break;
		}
	    }
	    if(flag==0) break;
	    ll temp = num-sub;
	    s = "";
	    while(temp) {
		s = s+(char)('0'+(temp%10));
		temp /= 10;
	    }
	    reverse(s.begin(),s.end());
	}
	cout<<"Case #"<<tc++<<": "<<s<<endl;
    }
}
