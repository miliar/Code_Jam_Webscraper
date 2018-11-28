
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
    freopen("codejam17a2.in","r",stdin);
    freopen("codejam17a2.out","w",stdout);
    int t; cin>>t;
    int tc=1;
    while(t--) {
	string s; cin>>s;
	int k; cin>>k;
	int ans = 0;
	int flag = 1;
	for(int i=0;i<s.length();i++) {
	    if(s[i]=='-') {
		if(i+k-1<s.length()) {
		    ans++;
		    for(int j=i,w=0;w<k;w++,j++) {
			if(s[j]=='-') s[j] = '+';
			else s[j] = '-';
		    }
		}
		else {
		    flag = 0;
		}
	    }
	}
	cout<<"Case #"<<tc++<<": ";
	if(flag) {
	    cout<<ans<<endl;
	}
	else {
	    cout<<"IMPOSSIBLE\n";
	}
    }
    return 0;
}
