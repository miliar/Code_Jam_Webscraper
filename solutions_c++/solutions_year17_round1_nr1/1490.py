#include<bits/stdc++.h>

#define speed ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define fname "A-large"
#define pb push_back
#define mp make_pair
#define ss second
#define ff first

using namespace std;

typedef long double ld;
typedef long long ll;
const int maxn = (1e5) + 10;
const int INF = (1e9);
const ll inf = (1e18);
const double eps = (1e-9);
const ld PI = acos(-1);

int t,n,m,cur;
char c[100][100],last;
int u[200];

int main(){    
    speed
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>n>>m;
		for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j){
			cin>>c[i][j];
		}
		for(int j=1;j<=m;++j){
			cur=1;
			for(int i=1;i<=n;++i){
				if(c[i][j]!='?'){
					u[j]=1;
					last=c[i][j];
					for(int k=cur;k<=i;++k)
					c[k][j]=c[i][j];
					cur=i+1;
				}
			}
			if(cur!=n+1)
			for(int k=cur;k<=n;++k)
			c[k][j]=last;
		}
		for(int r=1;r<=50;++r){
		for(int j=1;j<=m;++j){
	//		if(r==1)
	//		cout<<u[j]<<" "<<u[j+1]<<" "<<j<<"\n";
			if(!u[j]&&u[j-1]&&j!=1){
				for(int i=1;i<=n;++i)
				c[i][j]=c[i][j-1];
				u[j]=1;
			}
			else if(!u[j]&&u[j+1]&&j!=m){
				for(int i=1;i<=n;++i)
				c[i][j]=c[i][j+1];
				u[j]=1;
			}
		}
		}
		for(int i=0;i<=100;++i){
			u[i]=0;
		}
		cout<<"Case #"<<tt<<":\n";
		for(int i=1;i<=n;++i){
			for(int j=1;j<=m;++j)
			cout<<c[i][j];
			cout<<"\n";
		}
	}
	return 0;
}

