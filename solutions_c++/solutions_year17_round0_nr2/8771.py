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

#define sz size()

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
      lli n; cin>>n;
      string s;
       //cin>>s;
       lli nn=n;
       while(n!=0)
        {
         s+=(n%10+'0');
         n/=10;
        }
         reverse(s.begin(),s.end());

         int len=s.length();
         if(s.length()==1)
         {
           cout<<"Case #"<<c<<": "<<nn<<endl;
           continue;
         }

          lli   ba=0;
          lli num=0;
          lli ans=0;
          for(int i=0;i<len;i++)
          {
            if(s[i]>0)
            {
              if(i==0  || (s[i]>s[i-1]))
               {
                lli temp=ba;
                temp=temp*10+(s[i]-'0'-1);
                for(int  j=i+1;j<len;j++)
                 {
                  temp=temp*10+9;
                 }
                 ans=max(ans,temp);
               }
            }
            if(i!=0 && s[i]<s[i-1]) break;
            ba=ba*10+(s[i]-'0');
          //   cout<<"ba "<<ba<<endl;
          }
          ans=max(ans,ba);
          cout<<"Case #"<<c<<": "<<ans<<endl;
        }
}
