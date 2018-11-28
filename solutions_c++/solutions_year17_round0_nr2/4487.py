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


int main() { 

freopen("inpl.in","r",stdin);
freopen("opl.txt","w",stdout);	

 int t; cin>>t;  

repn(test,1,t) {

	 ll n; sll(n);
	 vi v;

	 ll x=n;
	 string ans=to_string(n);

	 while(x) {

       int p=x%10;
       x/=10;
       v.pb(p);
	 }

	 reverse(all(v));
	 int ind=-1;

	 rep(i,sz(v)-1)
       if(v[i+1]<v[i]) {

       	  ind=i;
       	  break;
       }

       if(ind==-1) {

       	  cout<<"Case #"<<test<<": "<<n<<"\n";
       	  continue;
       }

       if(v[ind]>1) {

          // ans[ind]=(char)(v[ind]-1)+'0';
            int index=ind;

           repd(i,ind-1,0)
            if(ans[i]==ans[i+1])
                  index=i;
            else
                  break;

            ans[index]=(char)(v[index]-1)+'0';

           repn(i,index+1,sz(v)-1)
            ans[i]='9';

            cout<<"Case #"<<test<<": "<<ans<<"\n";
       }

       else {

       	string s="";

       	  rep(i,sz(v)-1)
       	    s+='9';

       	    cout<<"Case #"<<test<<": "<<s<<"\n";
       }

}
     
return 0;
}
