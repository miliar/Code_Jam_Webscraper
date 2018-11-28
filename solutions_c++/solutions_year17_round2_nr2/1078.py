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

string res,ans;

struct data{
    int x;
    char y;
}ara[5];

bool cmp(data a,data b)
{
    return a.x>b.x;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    int t,T,N,R,O,Y,G,B,V,i;
    si(T);
    for(t=1;t<=T;t++){
        res = "";
        ans = "";
        cin >> N >> R >> O >> Y>> G>>  B>> V;

        ara[1].x = R;
        ara[1].y = 'R';

        ara[2].x = B;
        ara[2].y = 'B';

        ara[3].x = Y;
        ara[3].y = 'Y';

        sort(ara+1,ara+3+1,cmp);

        for(i=1;i<=ara[1].x;i++) res = res + ara[1].y;
        for(i=1;i<=ara[2].x;i++) res = res + ara[2].y;
        for(i=1;i<=ara[3].x;i++) res = res + ara[3].y;

        for(i=0;i<N;i++) ans += ".";


        int pos = 0,l,r,n = N;

        int it = 0;

        int cnt = 0;

        bool ase = true;

        while(true){
            pos %= N;
            l = ((pos-1)+N)%N;
            r = ((pos+1)+N)%N;
            if(ans[pos]=='.' && ans[l]!=res[it] && ans[r]!=res[it]){
                ans[pos] = res[it];
                it++;
                n--;
            }
            pos++;
            cnt++;
            if(n==0) break;
            if(cnt>10000000){
                ase = false;
                break;
            }
        }


        if(ase) cout << "Case #" << t << ": " << ans << "\n";
        else cout << "Case #" << t << ": " << "IMPOSSIBLE\n";

    }


    return 0;
}

