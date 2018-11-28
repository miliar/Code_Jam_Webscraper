#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <sstream>
#include <numeric>
#include <map>
#include <cmath>
#include <iomanip>
using namespace std;
#define forn(i,n) for(int i=0;i<n;i++)
#define forn1(i,n) for(int i=1;i<=n;i++)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef pair<int,int> pii;
int t,n;
#define PI 3.1415926535897
double dp[1001][1001];//last pancake placed
int main(){
	cin>>t;
	cout<<setprecision(16);
	forn1(i,t){
		int k;
		cin>>n>>k;
		forn(j,n)
			forn(m,k)dp[j][m]=0.0;
		pair<double,double> rh[1001];
		
		forn(j,n){
			double a,b;
			cin>>a>>b;
			rh[j]=mp(a,b);
		}
		sort(rh,rh+n,greater<pair<double,double> >());
		forn(j,n){
			dp[j][0]=max(dp[j][0],PI*rh[j].fi*rh[j].fi+2.0*PI*rh[j].fi*rh[j].se);
		}
		forn(q,k){
			forn(j,n){
				for(int m=j+1;m<n;m++){
					dp[m][q+1]=max(dp[m][q+1],dp[j][q]+2.0*PI*rh[m].fi*rh[m].se);
				}
			}
		}
/*		forn(j,n){
			forn(q,k){
				cout<<dp[j][q]<<" ";
			}
			cout<<endl;
		}*/
		double mx=0.0;
		forn(j,n){
			mx=max(mx,dp[j][k-1]);
		}
		cout<<"Case #"<<i<<": "<<mx<<endl;
	}
	return 0;
}