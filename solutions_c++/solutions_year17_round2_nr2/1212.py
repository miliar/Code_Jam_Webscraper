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
#define N 1004
const long long infl = 1e18+5;

ll m,n,p,q,x,y,k,mx =-1,mn=infl,f,val,sz,sm,cnt,ans,t=1,i,j,ind=-1;
int a[N] ;
int main(){
INP
if (fopen("inp.txt", "r")) {
    freopen("myfile.txt","w",stdout);
    freopen("inp.txt", "r", stdin);
}
cin>>t;
sz = t;
while(t--){
	std::vector<P> v;
	cin>>n;
	fr(i,0,6){
		cin>>x;
		v.pb({x,i});
	}
	sort(all(v),greater< P>());
	if(v[0].fs > n/2 ){
		cout<<"Case #"<<sz-t<<": IMPOSSIBLE\n";
		continue;
	}
	// ws(v);
	x  = 0 ; 
	fr(i,0,v.siz){
		val = v[i].fs;
		while(val--){
			a[x]  = v[i].sc ; 
			x += 2;
			if(x >= n )
				x = 1;
		}

	}
	cout<<"Case #"<<sz-t<<": ";
	char ch; 
	fr(i,0,n){
		if(a[i] == 0){
			ch ='R';
		}
		else if(a[i] == 2){
			ch ='Y';
		}
		else
			ch = 'B';
		cout<<ch;
	}
	cout<<"\n";	


}




return 0 ;
}