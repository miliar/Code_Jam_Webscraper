#include <bits/stdc++.h>

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
#define MAX             100010
#define MOD             1000000007
#define INF             2000000000

int setBit(int n,int pos){ return n = n | (1 << pos); } //sets the pos'th bit to 1
int resetBit(int n,int pos){ return n = n & ~(1 << pos); } //sets the pos'th bit to 0
bool checkBit(int n,int pos){ return (bool)(n & (1 << pos)); } //returns the pos'th bit

/******************************************************************************************/

priority_queue <int> q;

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);

    int t,T,n,k,x,y,z,i;
    cin >> T;
    for(t=1;t<=T;t++){
        cin >> n >> k;
        while(!q.empty()) q.pop();
        q.push(n);
        for(i=1;i<=k;i++){
            x = q.top();
            x--;
            q.pop();
            y = x/2;
            z = y;
            if(x%2)y++;
            q.push(z);
            q.push(y);
            if(i==k){
                printf("Case #%d: %d %d\n",t,y,z);
            }
        }
    }
    return 0;
}
