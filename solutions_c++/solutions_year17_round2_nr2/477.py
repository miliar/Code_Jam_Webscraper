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


int col[6];
int N;
int pos[20];
bool solve(int idx,int a,int b,int c)
{
    if(idx == N) {
        if(pos[0] == pos[idx-1]) return 0;
        return 1;
    }
    bool ret = 0;
    if(a && (idx == 0 || pos[idx-1] != 1)) {
        pos[idx] = 1;
        ret |= solve(idx+1, a-1,b,c);
        if(ret) return 1;
    }
    if(b && (idx == 0 || pos[idx-1] != 2)) {
        pos[idx] = 2;
        ret |= solve(idx+1, a,b-1,c);
        if(ret) return 1;
    }
    if(c && (idx == 0 || pos[idx-1] != 3)) {
        pos[idx] = 3;
        ret |= solve(idx+1, a,b,c-1);
        if(ret) return 1;
    }
    return 0;
}
int main()
{
//    for(int i=1;i<=10;i++){
//        for(int j=i;j<=10;j++){
//            for(int k=j;k<=10;k++) {
//                N = i + j + k;
//                if(N > 18) continue;
//                if(solve(0,i,j,k)) printf("%d %d %d\n",i,j,k);
//                //else
//            }
//        }
//    }
//
    READ;
    WRITE;
    int R,O,Y,G,B,V;
    int t,cs=0;
    cin>>t;
    while(t--) {
        cin>>N;
        cin >> R >> O >> Y >> G >>  B >> V;
        vector<int> v;
        v.push_back(R);
        v.push_back(Y);
        v.push_back(B);
        sort(all(v));
        if(v[0] + v[1] >= v[2]) {
            printf("Case #%d: ",++cs);
            int prv = -1;
            int fast = -1;
            for(int i=0;i<N;i++) {
                int iM = 0, id = -1;
                if(prv !=1 ) if(R > iM ) iM = R, id = 1;
                if(prv !=2 ) if(Y > iM ) iM = Y, id = 2;
                if(prv !=3 ) if(B > iM ) iM = B ,id = 3;
                if(prv != fast ) {
                    int k = 0;
                    if(fast == 1) k = R;
                    if(fast == 2) k = Y;
                    if(fast == 3) k = B;
                    if( k >= iM ) iM = k , id = fast;
                }
                if(id==1) {
                    R--;
                    printf("%c",'R');
                }
                if(id==2) {
                    Y--;
                    printf("%c",'Y');
                }
                if(id==3) {
                    B--;
                    printf("%c",'B');
                }
                prv = id;
                if(fast == -1 ) fast = prv;
            }
            printf("\n");
        }else printf("Case #%d: IMPOSSIBLE\n",++cs);
    }
    return 0;
}
