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

const int MAX = 200009;

char a[MAX];
char b[MAX];
int main()
{
  int i,j;
  test(){
    int k;
    scs(a);
    sc(k);
    strcpy(b,a);
    int fl = 1;
    int n = strlen(a);
    int ansl = 0,ansr = 0;
    for(i=0;i+k-1<n;i++){
      if(a[i]=='-' && i+k-1<n){
        for(j=i;j<=i+k-1;j++){
          a[j] = a[j] ^ '+' ^ '-'; 
        }
        ansl++;
      }
    }
    for(i=0;i<n;i++){
      if(a[i]=='-')
        ansl = -1;
    }
    int fr = 1;
    for(i=n-1;i-k+1>=0;i--){
      if(b[i]=='-' && i-k+1>=0){
        for(j=i;j>=i-k+1;j--){
          b[j] = b[j] ^ '+' ^ '-';
        }
        ansr++;
      }
    }
    for(i=0;i<n;i++){
      if(b[i]=='-')
        ansr = -1;
    }
    if(ansl==-1 && ansr==-1){
      printf("Case #%d: IMPOSSIBLE\n",tno);
    }else{
      printf("Case #%d: %d\n",tno,min(ansr,ansl));
    }
  }
  return 0;
}
