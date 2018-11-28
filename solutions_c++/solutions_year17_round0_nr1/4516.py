// AUTHOR: ARVIND NAIR

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pi;
typedef vector<int> vi;

#define TEST  int test_case; scanf("%d",&test_case); while(test_case--)
#define RT fprintf(stderr, "\nTIME = %lf\n", 1.0 * clock()/CLOCKS_PER_SEC);
#define rep(a,c)   for ( int (a)=0; (a)<(c); (a)++)
#define repn(a,b,c)  for ( int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for (  int (a)=(b); (a)>=(c); (a)--)
#define FOR(arr) for(auto &i:arr)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb push_back
#define mp make_pair
#define EPS (double)(1e-9)
#define MOD 1000000007
#define M(x,i) memset(x,i,sizeof(x))
#define CLR(x) x.clear()
#define sz(x) (int)(x.size())
#define si(n) scanf("%d",&n)
#define gi(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define gll(n) printf("%lld\n",n)

int a[1005];

int main() {

freopen("inp1l.in","r",stdin);
freopen("op1l.txt","w",stdout);  

 int t; cin>>t;


 repn(test,1,t) {

	M(a,0);

	 string s; cin>>s;
	 int k; cin>>k;
	 bool flag=true;
	 int sum=0,ans=0;

	 rep(i,sz(s)) {

	 	 a[i]=((s[i]=='+'?1:0)+sum)%2 !=1;
	 	 sum+=a[i]-(i>=k-1?a[i-k+1]:0);
	 	 ans+=a[i];

	 	 if(i>sz(s)-k and a[i]!=0) {

	 	 	 flag=false;
	 	 	 break;
	 	 }
	 }

	 cout<<"Case #"<<test<<": ";

	 if(flag)
	 	cout<<ans<<"\n";
	 else
	 	cout<<"IMPOSSIBLE\n";
}
     
return 0;
}
