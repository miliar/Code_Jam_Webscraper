#include<bits/stdc++.h>
using namespace std;
#define test() int t;scanf("%d",&t);for(int tno=1;tno<=t;tno++)
#define mp make_pair
#define pb push_back
#define wl(n) while(n--)
#define fi first
#define se second
#define all(c) c.begin(),c.end()
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi; 
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
#define sz(a) int((a).size())
#define ini(a,v) memset(a,v,sizeof(a))
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scs(s) scanf("%s",s);
#define gcd __gcd
#define debug() printf("here\n") 
#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define MOD 1000000007
#define inf ((1<<29)-1)
#define linf ((1LL<<60)-1)
const double eps = 1e-9;
//-----------------------------------------------------------------------------------------------

const int MAX = 29;

int main()
{
	int i,j,k;
	test(){
		ll n;
		scl(n);
		char a[MAX]={0};
		char b[MAX]={0};
		sprintf(a,"%lld",n);
		int len = strlen(a);
		int sm = 0;
		for(i=0;i<len;i++){
			int x = a[i] - '0';
			int y = x;
			while(x>=0){
				int f = 0;
				for(j=i+1;j<len;j++){
					if(f==0&&a[j]-'0'<x)
						break;
					if(a[j]-'0'>x){
						f = 1;
					}
				}
				if(sm==1){
					b[i] = '9';
					break;
				}
				if(x<a[i]-'0'||j==len){
					b[i] = x + '0';
					if(x<a[i]-'0')
						sm = 1;
					break;
				}

				x--;
			}
			//chk(i);chk2(b[i],sm);
		}
		ll ans = 0;
		for(i=0;i<len;i++){
			ans = ans*10 + (b[i]-'0');
		}
		printf("Case #%d: %lld\n",tno,ans);
	}
	return 0;
}