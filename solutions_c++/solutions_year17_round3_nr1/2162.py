//    AND NOW IT BEGINS      //
#include<bits/stdc++.h>
using namespace std;
#define SF(x)	scanf("%d", &x)
#define SFL(x) scanf("%lld",&x)
#define sf(x) scanf("%Lf",&x)
#define sc(x) scanf(" %c",&x)
#define PF(x)	printf("%d", x)
#define PFL(x) printf("%lld",x);
#define psp     printf(" ")
#define pnl     printf("\n")
#define pie     cout<<" # "<<endl
#define pii pair< ll, ll >
#define pb(x) push_back(x)
#define test int t; scanf("%d",&t);while(t--)
#define forall(i,a,b) for(int i=(a);i<=(b);++i)
#define gcd(a,b)   __gcd(a,b)
#define bss binary_search
#define ersort(x)       (sort((x).rbegin(), (x).rend()))
#define rev(v)      (reverse(v.begin(),v.end()))
#define vmax(v)     (*max_element(v.begin(),v.end()))
#define vmin(v)     (*min_element(v.begin(),v.end()))
#define MAX		400050
#define INF		1e12
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define mod     1000000007
#define ROUNDOFFINT(d) d = (int)((double)d + 0.5)
#define fi first
#define se second
inline bool isPowerOfTwo(int x){ return (x != 0 && (x&(x - 1)) == 0); }
typedef long double 		ll;
typedef unsigned long long	ull;
int dx[8] = {1 , 0 , -1 , 0 , 1 , -1 , -1 , 1};    // last 4 diagonal
int dy[8] = {0 , 1 , 0 , -1 , 1 , 1 , -1 , -1};
inline bool ispalin(string& str){ int n = str.length(); for (int i = 0; i < n / 2; i++) if (str[i] != str[n - i - 1]) return false; return true; }
void swapp(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int expFactor(int n, int p)
{
    int x = p;
    int exponent = 0;
    while ((n/x) > 0)
    {
        exponent += n/x;
        x *= p;
    }
    return exponent;
}
inline int countsetbit(int n)
{
    unsigned int count = 0;
    while (n)
    {
      n &= (n-1) ;
      count++;
    }
    return count;
}
inline int abs(int x){
	if(x<0)
	return -x;
	return x;
}
bool isPal(string ss){
    int len = ss.length();
    for(int i = 0 ; i<len/2 ; i++){
	int comp = len-i-1;
	if(ss[i]!=ss[comp])
		return false;
	}
    return true;
}
 
//     AND NOW IT ENDS        //
ll dp[1005][1005];
int n,k;
ll dp1[1001];
vector<pii> v(1001);
ll pi= 3.1415926535897932;

ll solve(int i,int c){
	if((i==n && c==k) || (c==k)){
		return 0.00000000000;
	}
	if(i==n){
		return -1.1e+16;
	}
	
	if(dp[i][c]!=-1)
	return dp[i][c];
	
	dp[i][c]=2.0000000*pi*v[i].fi*v[i].se+solve(i+1,c+1);
	dp[i][c]=max(dp[i][c],solve(i+1,c));
	
	return dp[i][c];
}

int main(){
	int t;
	cin>>t;
	for(int cc=1;cc<=t;cc++){
		SF(n);SF(k);
		
		for(int i=0;i<=n;i++){
			for(int j=0;j<=k;j++){
				dp[i][j]=-1;
			}
		}
		
		for(int i=0;i<n;i++){
			cin>>v[i].fi>>v[i].se;
			v[i].fi+=0.000000000000001;
			v[i].se+=0.000000000000001;
		}
		
		sort(v.begin(),v.begin()+n);
		reverse(v.begin(),v.begin()+n);
		
		
		ll height=0,ans=0;
		for(int i=0;i<n;i++){
			height=2*pi*v[i].fi*v[i].se+solve(i+1,1);
			ans=max(ans,pi*v[i].fi*v[i].fi+height);
		}
		cout<<"Case #"<<cc<<": ";
		printf("%0.7Lf\n",ans);
	}
}
