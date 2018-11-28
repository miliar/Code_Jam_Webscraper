/*             deepak gautam
	   Linkedin -https://www.linkedin.com/notifications/
  codechef - algorithmist2 ,codeforce - gautam27
  topcoder- gautam_27      ,spoj - nexus_d
  hackerearth-deepak.gautam.127648 , hackerrank- deepakgautam2701
   */
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define test() int t; cin>>t;while(t--)

#define si(x) scanf("%d",&x)
#define slli(x) scanf("%lld",&x)
#define sli(x) scanf("%ld",&x)


#define pfi(x) printf("%d\n",x)
#define pfli(x) printf("%ld\n",x)
#define pflli(x) printf("%lld\n",x)

#define abs(x) ((x)>0?(x):-(x))


#define TRI(a,b,c) mp(mp(a,b),c)
#define all(x) x.begin(),x.end()
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())



#define rep(i,a,b) for(int  i=(a);i<(b);i++)
#define repl(i,a,b) for(lli  i=(a);i<(b);i++)
#define rrep(i,a,b) for(int i=(b);i>=(a);i--)
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )

typedef pair<lli,lli> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
#define debug 0
inline int mult(int a , int b) { lli x = a; x *= lli(b); if(x >= mod) x %= mod; return x; }
inline int add(int a , int b) { return a + b >= mod ? a + b - mod : a + b; }
inline int sub(int a , int b) { return a - b < 0 ? mod - b + a : a - b; }
lli powmod(lli a,lli b) { if(b==0)return 1; lli x=powmod(a,b/2); lli y=(x*x)%mod; if(b%2) return (a*y)%mod; return y%mod; }
int read_int(){
	char r;bool start=false,neg=false;int ret=0;
	while(true){r=getchar();if((r-'0'<0 || r-'0'>9) && r!='-' && !start){continue;}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){	break;	}if(start)ret*=10;start=true;
		if(r=='-')neg=true;else ret+=r-'0';}if(!neg)return ret;else	return -ret;}
lli read_lli(){
 char r;bool start=false,neg=false;lli ret=0;
 while(true){r=getchar();if((r-'0'<0 || r-'0'>9) && r!='-' && !start){	continue;}
 if((r-'0'<0 || r-'0'>9) && r!='-' && start){	break;}if(start)ret*=10;
	start=true;if(r=='-')neg=true;else ret+=r-'0';}if(!neg)	return ret;else	return -ret;}


int used[1010];
int bac[1010];
int fo[1010];

int main()
{
 freopen("abc.txt","r",stdin);
 freopen("pqr.txt","w",stdout);
 int t;
  cin>>t;
  int c=0;
  while(t--)
   {
    c++;
   memset(used,0,sizeof used);
    int n,k; cin>>n>>k;

    for(int j=0;j<k;j++)
     {
    //  cout<<" place "<<j<<endl;
         bac[n+1]=n+1;
         for(int i=n;i>=0;i--)
          {
           if(used[i] )
            bac[i]=i;
            else
            {
            bac[i]=bac[i+1];
            }
          }

      int last=0;
      int mini=-1,maxi=-1;
      int idx=0;
     for(int i=1;i<=n;i++)
      {
         if(used[i] )
         {
          last =i;
          continue;
         }
         else
          {
            if(mini<min(i-last,bac[i]-i))
             {
                 idx=i;
                 mini=min(i-last,bac[i]-i);
                 maxi=max(i-last,bac[i]-i);
             }
             else if(mini==min(i-last,bac[i]-i) && maxi<max(i-last,bac[i]-i))
              {
                 idx=i;
                 mini=min(i-last,bac[i]-i);
                 maxi=max(i-last,bac[i]-i);

              }
          }
         // cout<<i<<" mini "<<mini<<" maxi "<<maxi<<"idx "<<idx<<endl;
      }
      // cout<<"fix "<<idx<<endl;


      used[idx]=1;
      if(j==k-1)
       {
          cout<<"Case #"<<c<<": "<<maxi-1<<" "<<mini-1<<endl;
       }
     }

    }

}
