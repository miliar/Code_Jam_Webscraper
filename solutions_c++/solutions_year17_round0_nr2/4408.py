#include<bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

#define modulo(S, N) ((S) & (N - 1)) // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

#define all(x) (x).begin(), (x).end()
#define unq(x) (x.resize(unique(all(x)) - x.begin()))

#define inf LLONG_MAX
#define mx  100005
#define mod 1000000007

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector< pll > vll;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef double D;
typedef long double LD;
//int dx[]= {0,0,-1,1,1,-1,1,-1};
//int dy[]= {-1,1,0,0,1,-1,-1,1};

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    ll t,tc=1,n;
    scanf("%lld",&t);

    while(tc<=t)
    {
        vector<ll> vt;
        scanf("%lld",&n);
        printf("Case #%lld: ",tc);
        while(n)
        {
            ll tmp = n;
            while(tmp)
            {
                vt.push_back(tmp%10);
                tmp/=10;
            }
            ll z = vt.size();
            bool flag =true;
            for(int i=1; i<z; i++)
            {
                if(vt[i]>vt[i-1])
                {
                    flag =false;
                    break;
                }
            }
            if(flag)
            {
                printf("%lld\n",n);
                break;
            }
            vt.clear();
            n--;
        }
        tc++;
    }
    return 0;
}
