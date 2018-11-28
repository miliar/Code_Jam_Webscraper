#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(i,n){ 0 == scanf("%d", &v[si]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 1005

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		ll n;
		cin>>n;
		vi v;
		while(n){
			v.pb(n%10);
			n/=10;
		}
		reverse(all(v));
		FOR(i, sz(v)-1){
			if(v[i]>v[i+1]){
				v[i]-=1;
				for(int j=i+1;j<sz(v);j++){
					v[j]=9;
				}
				i=-1;
			}
		}
		FOR(i,sz(v)){
			n*=10;
			n+=v[i];
		}
		cout<<"Case #"<<(t+1)<<": "<<n<<endl;
	}
	return 0;
}