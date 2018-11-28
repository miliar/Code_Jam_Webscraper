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
#define N 100010
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
inline void add(int &a,int b){a+=b;if(a>=mod)a-=mod;}


int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}

char s[1010];
int a[2010];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    //cerr<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,K,n,m;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%s%d",s,&K);
        n=strlen(s);
        rep(i,0,n+1)a[i]=0;
        int ans=0;
        rep(i,0,n-K+1){
            a[i+1]+=a[i];
            k=s[i]=='+'?1:0;
            if(a[i+1]&1)k^=1;
            if(!k){
                a[i+1]++,a[i+K+1]--;
                ans++;
            }
        }
        int ok=1;
        rep(i,n-K+1,n){
            a[i+1]+=a[i];
            k=s[i]=='+'?1:0;
            if(a[i+1]&1)k^=1;
            if(k==0){ok=0;break;}
        }
        if(!ok)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}