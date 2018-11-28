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
#define SIZE 100001

typedef long long  ll;
typedef unsigned long long ull;
typedef long double  ldo;
typedef double  db ;
using namespace std;
int a[SIZE];
map<int,int> M;
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
	int i,t,n,p;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		cin>>n>>p;
		M.clear();
		forp(i,1,n){
			cin>>a[i];
			M[a[i]%p]++;
		}
		int ans=M[0];
		if(p==2){
			ans += (M[1]+1)/2;
		}
		else{
			if(p==3){
				int mn = min(M[1],M[2]);
				int mx = max(M[1],M[2]);
				ans += mn;
				mx -= mn;
				ans += (mx+2)/3;
			}
			else{
				int m1 = M[1];
				int m2 = M[2];
				int m3 = M[3];
				ans += m2/2;
				int mn = min(M[1],M[3]);
				int mx = max(M[1],M[3]);
				ans += mn;
				mx -= mn;
				ans += (mx+3)/4;
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	return 0;
}
