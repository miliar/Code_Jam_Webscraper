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
int n;
string res;

int dp[22][12][3];

int call(int pos,int last,int soto)
{
    if(pos==n) return 1;
    if(dp[pos][last][soto]!=-1) return dp[pos][last][soto];
    int ret = 0;
    if(soto) return dp[pos][last][soto] = 1;
    else{
        for(int i=last;i<=(s[pos]-'0');i++){
            ret |= call(pos+1,i,(i!=(s[pos]-'0')));
        }
        return dp[pos][last][soto] = ret;
    }

}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t,T,i,j;
    cin >> T;
    for(t=1;t<=T;t++){
        SET(dp);
        cin >> s;
        res = "";
        n = s.size();
        bool soto = false;
        int last = 0;
        for(i=0;i<n;i++){
            if(soto){
                res = res + "9";
            }
            else{
                for(j=(s[i]-'0');j>=last;j--){
                    if(call(i+1,j,j!=(s[i]-'0'))){
                        soto = (j!=(s[i]-'0'));
                        res = res + (char)(j+'0');
                        last = j;
                        break;
                    }
                }
            }

        }
        cout << "Case #" << t << ": ";
        bool lead = true;
        for(i=0;i<n;i++){
            if(res[i]=='0' && lead) lead = false;
            else cout << res[i];
        }
        cout << endl;
    }
    return 0;
}
