#pragma comment(linker, "/STACK:102400000,102400000")
#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define x first
#define y second
#define pi acos(-1.0)
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
//#define dprintf(...) 
#define hash _hash
#define next _next
//#define dprintf(...) fprintf(outFile,__VA_ARGS__)
 
#define FOREACH(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
#define ull unsigned long long
#define ll long long
#define N 1000005
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
inline void add(int &a,int b){a+=b;while(a>=mod)a-=mod;}


int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}

int v[1010];
vi a[1010];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m=0,n,K;
    scanf("%d",&T);
    while(T--){
    	printf("Case #%d: ",++ca);
        scanf("%d%d%d",&n,&K,&m);
        rep(i,0,K)v[i]=0;
        rep(i,0,n)a[i].clear();
    	rep(i,0,m){
    		scanf("%d%d",&j,&k);k--;j--;
    		v[k]++;
    		a[j].pb(k);
    	}
    	int l=1;
    	rep(i,0,K)Max(l,v[i]);
    	int r=m,ans=0;
    	while(l<=r){
    		int x=(l+r)>>1;
    		bool ok=1;int s=0,need=0;
    		rep(i,0,n){
    			s+=x;
    			if(SZ(a[i])>s){
    				ok=0;break;
    			}
    			s-=SZ(a[i]);
    			need+=max(0,SZ(a[i])-x);
    		}
    		if(ok)r=x-1,ans=need;
    		else l=x+1;
    	}
    	printf("%d %d\n",r+1,ans);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}