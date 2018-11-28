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

int rem[10];

ll main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t,cc=0;
	cin>>t;	
	while (t--) {
		cc++;
		int n,p;
		cin>>n>>p;

		memset(rem,0,sizeof(rem));
		for (int i=0 ; i<n ; i++) {
			int x;
			cin>>x;
			rem[x%p]++;
		}
		if(p==2) {
			int ret=rem[0]+(rem[1]+1)/2;
			cout<<"Case #"<<cc<<": "<<ret<<endl;
		}
		else if(p==3) {
			int ret=rem[0];
			int bal=min(rem[1],rem[2]),bal2=max(rem[1],rem[2]);
			int num=bal;
			if(bal2-bal!=0) {
				num=num+(bal2-bal+2)/3;
			}
			ret=ret+num;
			cout<<"Case #"<<cc<<": "<<ret<<endl;
		}
	}
}