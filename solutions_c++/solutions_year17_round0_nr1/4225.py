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
#define MAX             250010
#define MOD             1000000007
#define INF             2000000000

int setBit(int n,int pos){ return n = n | (1 << pos); } //sets the pos'th bit to 1
int resetBit(int n,int pos){ return n = n & ~(1 << pos); } //sets the pos'th bit to 0
bool checkBit(int n,int pos){ return (bool)(n & (1 << pos)); } //returns the pos'th bit

/******************************************************************************************/

string s;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t,T,k,n,res,i,j,l;
    cin >> T;
    for(t=1;t<=T;t++){
        cin >> s >> k;
        n = s.size();
        res = 0;
        for(i=0;i<n-k+1;i++){
            if(s[i]=='-'){
                res++;
                for(j=i,l=0;l<k;j++,l++){
                    if(s[j]=='+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }

        bool pos = true;
        for(i=0;i<n;i++) if(s[i]=='-') pos = false;

        if(pos) printf("Case #%d: %d\n",t,res);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
