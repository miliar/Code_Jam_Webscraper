#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define FOR(I,A,B)              for(long long I = (A); I < (B) ; ++ I)
#define REP(i,n)                for( long long i=0 ; i < n ; i++ )
#define mp                      make_pair
#define pb                      push_back
#define all(x)                  (x).begin(),(x).end()
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define F                       first
#define S                       second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   long long x;scanf("%d",&x)
#define in2(x,y)                input(x), input(y)
#define in3(x,y,z)              input(x), input(y),input(z)
#define ins(x)                  scanf("%s",x)
#define ind(x)                  scanf("%lf",&x)
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
#define IO                      ios_base::sync_with_stdio(0);cin.tie(0)
#define READ                    freopen("in.txt","r",stdin)
#define WRITE                   freopen("out.txt","w",stdout)

template<class T > void input(T &x)
{
    char c = getchar();
    x = 0;
    for(; (c<48 || c>57); c = getchar());
    for(; c>47 && c<58; c = getchar()) {
        x = (x<<1) + (x<<3) + c - 48;
    }
}
inline long long bigmod(long long p,long long e,long long M)
{
    long long ret = 1;
    for(; e > 0; e >>= 1) {
        if(e & 1) {
            ret = (ret * p) % M;
        }
        p = (p * p) % M;
    }
    return ret;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0) {
        return a;
    }
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}

/***************************** END OF TEMPLATE *******************************/

const int N = 1001;
int cus[N];
int B[N],P[N];
int t,cs=0,n,c,m,b,p;
vector<int> tic[N];
int can(int r)
{
    vector<int> in(n+1,0);
    set<int> Row;
    for(int i=0;i<r;i++) Row.insert(i);
    vector< vector<int> > V(n+1,vector<int>(r,0));
    set<int> col[1001];
    int ret = 0;
    for(int i=1;i<=c;i++){
        for(auto x: tic[i]) {
            if(in[x] < r ) {
                bool f=0;
                int c = -1;
                for(int j=0;j<r;j++) if(V[x][j] == 0) {
                    V[x][j] = i;
                    c = j;
                    f=1;
                    break;
                }
                if(f==0)return -1;
                in[x]++;
                col[c].insert(i);
                if(in[x]==r) {
                    Row.erase(x);
                }
            }
            else {
                bool f = 0;
                for(int c= 0;c<r;c++){
                    if(col[c].count(i)==0){
                        int oo = -1;
                        for(auto r: Row) {
                            if(r < x ) {
                                in[r] ++;
                                f=1;
                                V[r][c] = i;
                                col[c].insert(i);
                                oo = r;
                                break;
                            }
                        }
                        if(f) {
                            if(in[oo] == r ) {
                                Row.erase(oo);
                            }
                            break;
                        }
                    }
                }
                if(f==0) return -1;
                ret++;
            }
        }
    }
    return ret;

}

int main()
{
    READ;
    WRITE;
    cin>>t;
    while(t--){
        in3(n,c,m);
        map<int,int> Map;
        int one = 0;
        for(int i=0;i<m;i++){
           in2(P[i],B[i]);
           Map[B[i]]++;
           if(P[i]==1) one++;
           tic[B[i]].push_back(P[i]);

        }
        for(int i=1;i<=c;i++) sort(all(tic[i]));
        int low=1,high=m,mid,ans=m,q=0;
        for(auto a: Map) low=  max(low, a.second);
        low = max(low,one);
        while(low<=high){
            mid= (low+high)/2;
            int r = can(mid);
            if(r >= 0) {
                ans = mid;
                q = r;
                high=mid-1;
            }else low=mid+1;
        }
        printf("Case #%d: %d %d\n",++cs,ans,q);
        for(int i=1;i<=c;i++) tic[i].clear();
        Map.clear();

    }

}

