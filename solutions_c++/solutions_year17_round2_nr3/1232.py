// avvinci - April 17 
// #include"prettyprint.hpp"
#include<bits/stdc++.h>
using namespace std;
typedef pair<long long int , long long int> P;
#define mod 1000000007 
#define pb push_back
#define mk make_pair
#define fs first
#define sc second
#define ll long long int
#define fr(it,st,en) for(it=st;it<en;it++)
#define all(container) container.begin(),container.end()
#define INP ios_base::sync_with_stdio(false);cin.tie(NULL);
#define ws(x) cout << #x << " = " << x << endl
#define siz size()
#define N 104
const long long infl = 1e13+5;

ll m,n,p,q,x,y,k,mx =-1,mn=infl,f,val,sz,sm,cnt,ans,t=1,i,j,ind=-1;
double e[N],s[N],ps[N];
double d[N][N] ,dp[N][N];

double rec(int ind , int hi){
	if(ind == n-1 )
		return 0 ; 
	if(dp[ind][hi] != -1 )
		return dp[ind][hi];
	double re = infl ;
	double rem = ps[ind+1]-ps[ind] ;

	if(e[hi]  >=  (ps[ind+1] - ps[hi]) ){

		re = min(re , (rem)/s[hi] + rec(ind+1,hi) );
		re = min(re , (rem)/s[hi] + rec(ind+1,ind+1) );
		// ws(re);
	} 
	
	dp[ind][hi] = re;
	return re;

}
int main(){
INP
if (fopen("inp.txt", "r")) {
    freopen("myfile.txt","w",stdout);
    freopen("inp.txt", "r", stdin);
}


cin>>t;
sz = t;
while(t--){
	cin>>n>>q;
	fr(i,0,N){
		fr(j,0,N){
			dp[i][j] = -1;
		}
	}
	fr(i,0,n){
		cin>>e[i]>>s[i];
	}
	fr(i,0,n){
		fr(j,0,n){
			cin>>d[i][j];
		}
	}
	ps[0] = 0 ;
	fr(i,1,n+1){
		ps[i] = ps[i-1] + d[i-1][i];
		// ws(ps[i]);
	}
	cin>>x>>y;
	cout<<"Case #"<<sz-t<<": ";
	cout<<fixed<<setprecision(7)<<rec(0,0);
	cout<<"\n";

}


return 0 ;
}