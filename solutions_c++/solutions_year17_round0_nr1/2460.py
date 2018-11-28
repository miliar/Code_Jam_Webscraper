#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define FOR(I,A,B)              for(int I = (A); I < (B) ; ++ I)
#define REP(i,n)                for( int i=0 ; i < n ; i++ )
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
#define Di(x)                   int x;scanf("%d",&x)
#define in(x)                   input(x)
#define in2(x,y)                input(x), input(y)
#define in3(x,y,z)              input(x), input(y),input(z)
#define ins(x)                  scanf("%s",x)
#define ind(x)                  scanf("%lf",&x)
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
#define IO                      ios_base::sync_with_stdio(0);cin.tie(0)
#define READ                    freopen("/Users/matrixcode/Desktop/in.txt","r",stdin)
#define WRITE                   freopen("/Users/matrixcode/Desktop/out.txt","w",stdout)

template<class T > void input(T &x){
    char c = getchar();x = 0;
    for(;(c<48 || c>57);c = getchar());
    for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}
}
inline long long bigmod(long long p,long long e,long long M){
    long long ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

/***************************** END OF TEMPLATE *******************************/

const int N = 1001;
int main()
{
    READ;
    WRITE;
    int cs= 0;
    Di(t);
    while(t--){
        string s;
        int k;
        cin>>s>>k;
        int tot = 0;
        bool flag= 1;
        for(int i= 0;i < s.size();i++) {
            if(s[i]=='-') {
                tot++;
                if(i + k - 1 < s.size()) {
                    for(int j=i, p = 0; p < k; j++,p ++) {
                        s[j]= (s[j]=='+')?'-':'+';
                    }
                }
                else {
                    flag = 0;
                    break;
                }
            }
            if(!flag) break;
        }
        if(flag) printf("Case #%d: %d\n",++cs,tot);
        else printf("Case #%d: IMPOSSIBLE\n",++cs);
    }
    return 0;
}
