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
	for(int i=1;i<65;i++) POWER[i]=POWER[i-1]<<1LL;
}

ll main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	precompute();
	int t,cc=1;
	cin>>t;

	while (t--) {
		int n,k;
		cin>>n>>k;

		int sum=0,num=-1,bum=0;
		for (int i=0 ; i<62 ; i++) {
			sum+=POWER[i];
			if(sum<k) {
				bum=sum;
				num=i;
			}
		}
		int val=POWER[num+1];
		n-=bum;
		int b=n/val;
		cout<<"Case #"<<cc<<": ";
		cc++;
		k-=bum;
		if(n%val<k) {
			int ans=b/2,ans1=(b-1)/2;
			cout<<ans<<" "<<ans1<<endl;
		}
		else {
			b++;
			int ans=b/2,ans1=(b-1)/2;
			cout<<ans<<" "<<ans1<<endl;
		}
	}
}