#include <bits/stdc++.h>
using namespace std;

typedef int ll;

#define int long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define sz(x) ((int)x.size())
#define all(x) x.begin(),x.end()

typedef pair<int,int>pii;
typedef pair<int,pair<int,int> > piii;

const int mod=1e9+7;

int POWER[65];
int power(int a, int b) {int ret=1;while(b) {if(b&1) ret*=a;a*=a;if(ret>=mod) ret%=mod;if(a>=mod) a%=mod;b>>=1;}return ret;}
int inv(int x) {return power(x,mod-2);}

void precompute() {
	POWER[0]=1;
	for(int i=1;i<63;i++) POWER[i]=POWER[i-1]<<1LL;
}
char str[1005];

ll main() {
	// freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		++cc;
		scanf("%s",str+1);
		int len = strlen(str+1);
		int k;
		scanf("%lld",&k);
		int ans=0;
		for(int i=1;i<=len-k+1;i++) {
			if(str[i]=='-') {
				ans++;
				int cnt=k;
				for(int j=i;cnt--;j++) {
					if(str[j]=='+') str[j]='-';
					else str[j]='+';
				}
			}
		}
		bool f = true;
		for(int i=1;i<=len;i++) if(str[i]=='-') f=false;
		if(f) cout<<"Case #"<<cc<<": "<<ans<<"\n";
		else cout<<"Case #"<<cc<<": "<<"IMPOSSIBLE"<<"\n";
	}
}