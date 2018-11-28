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
sz =  t;
while(t--){
	string s;
	cin>>s;
	n = (ll)s.siz;
	
	sm = 20;
	while(sm--){

		ind = -1;
		fr(i,0,n-1){
			if(s[i]-'0' > s[i+1] - '0' ){
				ind = i ;
				break;
			}

		}
		if(ind != -1 ){
			s[ind] =  (char)( s[ind] -1) ;
			fr(i,ind+1,n)
				s[i] = '9';

		}
		

	}

	ind = 0 ;
	while(ind < n && s[ind] == '0')
		ind++;
	cout<<"Case #"<<sz-t<<": ";
	// ws(s);
	fr(i,ind,n)
		cout<<s[i];
	cout<<"\n";

}



return 0 ;
}