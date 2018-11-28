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

priority_queue<ll> q;

int main() {

freopen("inp22.in","r",stdin);
freopen("op22.txt","w",stdout);   

int t; cin>>t;

repn(test,1,t) {

	ll n,k; cin>>n>>k;
   
   while(!q.empty())
   	q.pop();

   q.push(n);
   int p;

   while(k--) {

   	   p=q.top();
   	  q.pop();

   	  if(p&1)
   	  	q.push(p/2),q.push(p/2);
   	  else
   	  	q.push(p/2-1),q.push(p/2);
   }

   cout<<"Case #"<<test<<": ";

  if(p&1)
  	cout<<p/2<<" "<<p/2<<"\n";
  else
  	cout<<p/2<<" "<<p/2-1<<"\n";

}
     
return 0;
}
