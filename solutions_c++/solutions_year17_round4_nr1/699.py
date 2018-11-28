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


int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    //cout<<setprecision(9)<<fixed;
    int T,i,j,k,ca=0,m=0,n,K;
    scanf("%d",&T);
    while(T--){
    	printf("Case #%d: ",++ca);
        scanf("%d%d",&n,&K);
        int v[5]={0},ans=0;
        rep(i,0,n){
            scanf("%d",&k);
            k%=K;
            v[k]++;
        }
        ans+=v[0];
        if(K==2){
            ans+=v[1]/2;
            if(v[1]&1)ans++;
        }
        else if(K==3){
            k=min(v[1],v[2]);
            v[1]-=k,v[2]-=k;
            ans+=k;
            ans+=v[1]/3+v[2]/3;
            v[1]%=3,v[2]%=3;
            ans+=(v[1]+v[2])>0;
        }
        else{
            int r=min(v[1],v[3]),l=v[2]/2,res=0;
            rep(i,0,r+1){
                rep(j,0,l+1){
                    int cnt=i+j;
                    int n1=v[1]-i,n3=v[3]-i,n2=v[2]-j*2;
                    int z=min(n1/2,n3/2);
                    cnt+=z;
                    n1-=z*2,n3-=z*2;
                    z=min(n1/2,n2);
                    cnt+=z;
                    n1-=2*z,n2-=z;
                    z=min(n3/2,n2);
                    cnt+=z;
                    n3-=2*z,n2-=z;
                    cnt+=n1/4;
                    cnt+=n3/4;
                    n1%=4,n3%=4;
                    cnt+=(n1+n3)>0;
                    Max(res,cnt);
                }
            }
            ans+=res;
        }
        printf("%d\n",ans);
    }
    //cerr<<clock()*1./CLOCKS_PER_SEC<<"ms\n";
    return 0;
}