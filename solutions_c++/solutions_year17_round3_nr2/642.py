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

pii DP[1447][727][5];
int num[1445];

pii go(int curr , int a , int las) {
	// cout<<curr<<" "<<a<<" "<<las<<endl;
	if(curr==1441 && a==0) {
		// cout<<"Hello\n";
		return mp(0,las);
	}
	if(a<0 || curr==1441) {
		return mp(-2,-1);
	}

	if(DP[curr][a][las].ff!=-1)
		return DP[curr][a][las];

	if(num[curr]==0) {
		pii ret;
		if(las==1) {
			ret=go(curr+1,a-1,1);
			pii val=go(curr+1,a,2);
			if(val.ff!=-2)	val.ff++;
			if((val.ff<ret.ff && val.ff!=-2) || ret.ff==-2) {
				DP[curr][a][las]=val;
				return val;
			}
			DP[curr][a][las]=ret;
			return ret;
		}

		ret=go(curr+1,a,2);
		pii val=go(curr+1,a-1,1);
		if(val.ff!=-2)	val.ff++;
		if((val.ff<ret.ff && val.ff!=-2) || ret.ff==-2) {
			DP[curr][a][las]=val;
			return val;
		}
		DP[curr][a][las]=ret;
		return ret;
	}
	if(num[curr]==1) {
		if(las==1) {
			pii ret=go(curr+1,a,2);
			if(ret.ff!=-2)	ret.ff+=1;
			DP[curr][a][las]=ret;
			return ret;
		}
		else {
			pii ret=go(curr+1,a,2);
			DP[curr][a][las]=ret;
			return ret;
		}
	}
	if(num[curr]==2) {
		if(las==1) {
			pii ret=go(curr+1,a-1,1);
			DP[curr][a][las]=ret;
			return ret;
		}
		else {
			pii ret=go(curr+1,a-1,1);
			if(ret.ff!=-2)	ret.ff+=1;
			DP[curr][a][las]=ret;
			return ret;
		}
	}

}
ll main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t,cc=0;
	cin>>t;

	while (t--) {

		for (int i=0 ; i<=1445 ; i++) {
			for (int j=0 ; j<=725 ; j++) {
				DP[i][j][0]=mp(-1,-1);
				DP[i][j][1]=mp(-1,-1);
				DP[i][j][2]=mp(-1,-1);
			}
		}
		memset(num,0,sizeof(num));
		int a,b;
		cin>>a>>b;

		for (int i=0 ; i<a ; i++) {
			int x,y;
			cin>>x>>y;

			for (int j=x ; j<y ; j++)	num[j]=1;
		}
		for (int i=0 ; i<b ; i++) {
			int x,y;
			cin>>x>>y;

			for (int j=x ; j<y ; j++)	num[j]=2;
		}

		pii ans1=mp(-1,-1);
		if(num[1]!=1) {
			ans1=go(2,719,1);
			if(ans1.ss!=1 && ans1.ff>=0) {
				ans1.ff++;
			}
			// cout<<ans1.ff<<" "<<ans1.ss<<endl;
		}
		pii ans2=mp(-1,-1);
		if(num[1]!=2) {
			for (int i=0 ; i<=1445 ; i++) {
				for (int j=0 ; j<=725 ; j++) {
					DP[i][j][0]=mp(-1,-1);
					DP[i][j][1]=mp(-1,-1);
					DP[i][j][2]=mp(-1,-1);
				}
			}
			ans2=go(2,720,2);
			// cout<<ans2.ff<<" "<<ans2.ss<<endl;
			if(ans2.ss!=2 && ans2.ff>=0) {
				ans2.ff++;
			}
		}
		int ma=max(ans1.ff,ans2.ff),mi=min(ans1.ff,ans2.ff);
		// cout<<ma<<" "<<mi<<endl;
		cc++;
		if(mi<0)
			cout<<"Case #"<<cc<<": "<<ma<<endl;
		else
			cout<<"Case #"<<cc<<": "<<mi<<endl;

	}
}