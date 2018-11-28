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
sz = t;
while(t--){
	f = 0 ;
	vector<int> v;
	ans = 0;
	string s;
	cin>>s>>k;
	n = (ll)s.siz;
	fr(i,0,s.siz){
		if(s[i] == '+')
			v.pb(1);
		else
			v.pb(0);
	}

	fr(i,0,v.siz){
		if(v[i] == 0){
			fr(j,i,i+k){
				if(j >= n )
				{
					f = 1;
					break;
				}

				v[j] ^= 1;
			}
			ans++;
		}
	}


	cout<<"Case #"<<sz-t<<": ";
	if(f){
		cout<<"IMPOSSIBLE\n";	
	}
	else
		cout<<ans<<"\n";
}



return 0 ;
}