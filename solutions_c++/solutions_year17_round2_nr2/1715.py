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
/* prime*/
lli pr[1000000];
void prime(int sz)
 {pr[0]=1;pr[1]=1;for(int i=2;i<=sz;i++){if(!pr[i]) {for(int j=2;j*i<=sz;j++) {pr[i*j]=1;}}}}

/* comb* ncr*/
lli  comb[1001][1001];
lli combination()
  {for(int i = 0; i < 1000; i++) {comb[i][0] = 1;for(int j = 1; j <= i; j++)comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;}}
  
/*gcd*/
lli gcd(lli a, lli b){ if(b)return gcd(b,a%b); return a;}

/*mulmod*/
lli mulmod ( lli a , lli b,lli mod_val)  
{lli ret = 0;while(b){if(b&1){ret += a;if(ret >= mod_val)ret %= mod_val;}a = a + a;if(a >= mod_val) a %= mod_val;b >>= 1;}return ret;}
  
/* prime factor of all numbers f+rom 1 to till n */;
bool  factu[10000010];vector<int> fact[10000010];
int  factor(int  n)
 {fact[1].push_back(1);for(int i=2;i<=n;i++){ if(!factu[i]){for(int j=i;j<=n;j+=i){factu[j]=1;fact[j].push_back(i);}}}}
 


int main()
{
	 freopen("B-small-attempt4.in","r",stdin);
  freopen("pqr.txt","w",stdout);
	 int t;
	  cin>>t;
	  int c=0;
	  while(t--)
	   {
	   	 c++;
	   	 int n;
	   	  cin>>n;
	   	  int r,y,b;
	   	  int o,v,g;
	   	  //N, R, O, Y, G, B, and V
	   	  cin>>r>>o>>y>>g>>b>>v;
	   	 string s="";
	   	 bool poss=true;
	   	  //cout<<" r "<<r<<" y "<<y<<" b "<<b<<endl;
	   	 for(int i=0;i<n;i++)
	   	     {
	   	     	if(!poss) break;
	   	        if(i==0)
	   	            {
	   	            	 if(r>y && r>b) 
	   	            	 {
	   	            	 	s+='R'; 
	   	            	 	r--;
							}
	   	            	 else if(y>r && y>b) 
	   	            	 {
	   	            	 	s+='Y';
	   	            	 	y--;
							}
	   	            	 else if(b!=0)
	   	            	    {
	   	            	 	s+='B';
	   	            	 	b--;
							}
							else poss=false;
	   	         	
					}
					else
					{
						 if(s[i-1]=='R')
						  {
						  	 if(b>y)
						  	    {
						  	  	   s+='B';
						  	  	    b--;
								}
								else if(y!=0)
								 {
								 	  s+='Y';
								 	  y--;
								 }
								 else if(i==n-1 && r!=0)
								 {
								 	 s+='R';
								 	  r--;
								 }
								 else
								 {
								 	poss=false;
								 }
						  	  
						  }
						  
						  
						  if(s[i-1]=='Y')
						  {
						  	 if(b>r)
						  	    {
						  	  	    s+='B';
						  	  	    b--;
								}
								else if(r!=0)
								 {
								 	  s+='R';
								 	  r--;
								 }
								 else if(i==n-1 && y!=0)
								 {
								 	 s+='Y';
								 	 y--;
								 }
								 else
								 {
								 	poss=false;
								 }
						  	  
						  }
						  
						  
						  
						  if(s[i-1]=='B')
						  {
						  	 if(r>y)
						  	    {
						  	  	   s+='R';
						  	  	    r--;
								}
								else if(y!=0)
								 {
								 	  s+='Y';
								 	  y--;
								 }
								 else if(i==n-1 && b!=0)
								 {
								 	 s+='B';
								 	 b--;
								 }
								 else
								 {
								 	poss=false;
								 }
						  	  
						  }
						   
					}
	   	      
	   	    //   cout<<i<<" "<<s<<endl;
	   	  	
			 }
			               if( s.length()==n && s[0]==s[n-1])
						    {
						    	 int p=false;
						    	 for(int i=1;i<n-1;i++)
						    	  {
						    	  	 if(s[i]!=s[n-1] && s[i-1]!=s[n-1] && (s[i+1]!=s[n-1]  || i+1==n-1)&& (s[n-2]!=s[i] || n-2==i))
						    	  	   {
						    	  	   	swap(s[i],s[n-1]);
						    	  	   	p=true;
						    	  	   	break;
									   }
								  }
								  if(!p)
								  {
								  	poss=false;
								  }
							}
			  if(!poss || s.length()!=n)
			   {
			   	 cout<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
			   }
			   else
			   {
			   	 cout<<"Case #"<<c<<": "<<s<<endl;
			   }
	   	  
	   }
	 
}

