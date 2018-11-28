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
#define N 1000004
const long long infl = 1e18+5;

ll m,n,p,q,x,y,k,mx =-1,mn=infl,f,val,sz,sm,cnt,ans,t=1,i,j,ind=-1;
ll a[N] ;
int main(){
INP
if (fopen("inp.txt", "r")) {
    freopen("myfile.txt","w",stdout);
    freopen("inp.txt", "r", stdin);
}

cin>>t;
sz=t;
while(t--){
	cin>>n>>k;
	priority_queue< int  > pq; 
	pq.push(n);
	while(k--){
		val = 	pq.top();
		// ws(val);
		pq.pop();
		x= val/2; 
		y = (val-1)/2 ;
		pq.push(x);
		pq.push(y);
	}

	cout<<"Case #"<<sz-t<<": "<<x<<" "<<y<<"\n";
}




return 0 ;
}