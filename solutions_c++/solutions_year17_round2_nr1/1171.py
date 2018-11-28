#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define si(a)           scanf("%d",&a)
#define sii(a,b)        scanf("%d %d",&a,&b)
#define siii(a,b,c)     scanf("%d %d %d",&a,&b,&c)

#define sl(a)           scanf("%I64d",&a)
#define sll(a,b)        scanf("%I64d %I64d",&a,&b)
#define slll(a,b,c)     scanf("%I64d %I64d %I64d",&a,&b,&c)

#define pb              push_back
#define PII             pair <int,int>
#define PLL             pair <ll,ll>
#define mp              make_pair
#define xx              first
#define yy              second
#define all(v)          v.begin(),v.end()

#define CLR(a)          memset(a,0,sizeof(a))
#define SET(a)          memset(a,-1,sizeof(a))

#define eps             1e-9
#define PI              acos(-1.0)
#define MAX             200010
#define MOD             1000000007
#define INF             2000000000

int setBit(int n,int pos){ return n = n | (1 << pos); } //sets the pos'th bit to 1
int resetBit(int n,int pos){ return n = n & ~(1 << pos); } //sets the pos'th bit to 0
bool checkBit(int n,int pos){ return (bool)(n & (1 << pos)); } //returns the pos'th bit

/******************************************************************************************/

long double pos[1010],sp[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t,T,d,n,i;
    long double D;
    si(T);
    for(t=1;t<=T;t++){
        cin >> D >> n;
        long double res = 0,x;
        for(i=1;i<=n;i++){
            cin >> pos[i] >> sp[i];
            x = (D-pos[i])/sp[i];
            res = max(res,x);
        }
        res = D/res;
        cout << setprecision(8) << fixed << "Case #" << t << ": " << res << "\n";
    }


    return 0;
}

