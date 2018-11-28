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
#define N 10004
const long long infl = 1e18+5;

ll m,n,p,q,x,y,mn=infl,f,val,sz,sm,cnt,t=1,i,j,ind=-1;
double s[N] , k[N] ,d ;
double mx , ans;
int main(){
INP
if (fopen("inp.txt", "r")) {
    freopen("myfile.txt","w",stdout);
    freopen("inp.txt", "r", stdin);
}

cin>>t;
sz =t;
while(t--){
	cin>>d>>n;
	ans = 0 ;
	fr(i,0,n){
		cin>>k[i]>>s[i];
		mx = (d-k[i])/s[i]; 
		ans = max(ans, mx);
	}
	cout<<"Case #"<<sz-t<<": ";
	cout<<fixed<<setprecision(7)<< (d/ans);
	cout<<"\n";

}



return 0 ;
}