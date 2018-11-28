#include<bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define len(s) s.length()
#define forp(i,a,b) for( i=a;i<=b;i++)
#define rep(i,n)    for( i=0;i<n;i++)
#define ren(i,n)    for( i=n-1;i>=0;i--)
#define forn(i,a,b) for( i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define b(v) v.begin()
#define e(v) v.end()
#define mem(n,m) memset(n,m,sizeof(n))
#define lb lower_bound
#define ub upper_bound
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>
#define gl(cin,s)  getline(cin,s);
#define bitc(n) __builtin_popcountll(n)
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++) 

#define boost ios_base::sync_with_stdio(0)
#define MOD 1000000007
#define EPSILON 1e-9
#define PI 3.14159265358979323846
#define SIZE 100

typedef long long  ll;
typedef unsigned long long ull;
typedef long double  ldo;
typedef double  db ;
using namespace std;
ll pack[SIZE][SIZE];
ll req[SIZE];
ll start[SIZE];
int main()
{  	
	/* #ifndef ONLINE_JUDGE
	freopen(fi, "r", stdin);
	#endif */
	freopen("route.in","r",stdin);
	freopen("route.out","w",stdout);
	//cin.ignore();
	//cin.clear();
	boost;
	//cin.tie(0);
	//cout<<"Case "<<tt<<": ";
	ll i,j,n,p,t;
	cin>>t;
	for(ll tt=1;tt<=t;tt++){
		cin>>n>>p;
		forp(i,1,n){
			cin>>req[i];
			start[i]=1;
		}
		forp(i,1,n){
			forp(j,1,p){
				cin>>pack[i][j];
			}
			sort(pack[i]+1,pack[i]+1+p);
		}
		ll fans = 0;
		ll X=1;
		bool is = false;
		while(1){
			//cout<<X<<endl;
			ll foo = INT_MAX;
			forp(i,1,n){
				ll temp = req[i]*X;
				ll mn = ceil(0.9*temp*1.000);
				ll mx = 1.1*temp;
				
				ll val = lb(pack[i]+start[i],pack[i]+1+p,mn)-pack[i];
				start[i]=val;
				if(start[i]>p){
					is=true;
					break;
				}
				//cout<<temp<<" "<<mn<<" "<<mx<<" "<<val<<endl;
				val = ub(pack[i]+start[i],pack[i]+1+p,mx)-pack[i];
				val--;
				//cout<<val<<endl;
				foo = min(foo,val-start[i]+1);
				//cout<<foo<<endl;
			}
			if(is)
			break;
			fans+=foo;
			forp(i,1,n){
				start[i]+=foo;
			}
			X++;
		}
		cout<<"Case #"<<tt<<": "<<fans<<endl;
	}
	return 0;
}
