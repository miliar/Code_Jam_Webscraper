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
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    ll t,tc=1,n,k;
    scanf("%lld",&t);
    while(tc<=t)
    {
        scanf("%lld %lld",&n,&k);
        map< ll, ll> mp;
        map< ll, ll>::iterator it;
        vll vt;
        printf("Case #%lld: ",tc);
        mp[n]++;
        bool flag = false;
        while(true)
        {   ll p,q;
            for(it=mp.begin(); it!=mp.end(); it++)
            {
                p = it->first;
                q = it->second;
                vt.push_back(pll(p,q));
            }
            sort(vt.rbegin(),vt.rend());
            mp.clear();
            ll z = vt.size();
            for(int i=0; i<z; i++)
            {
                if(vt[i].second < k)
                {
                    k -= vt[i].second;
                    if(vt[i].first%2)
                    {
                        mp[vt[i].first/2] += vt[i].second*2;
                    }
                    else
                    {
                        mp[vt[i].first/2] += vt[i].second;
                        mp[vt[i].first/2-1] += vt[i].second;
                    }
                }
                else
                {
                    if(vt[i].first%2)
                    {
                        printf("%lld %lld\n",vt[i].first/2,vt[i].first/2);
                        flag = true;
                        break;
                    }
                    else
                    {
                        printf("%lld %lld\n",vt[i].first/2,vt[i].first/2-1);
                        flag = true;
                        break;
                    }
                }
            }
            vt.clear();
            if(flag)
                break;
        }

        tc++;
    }
    return 0;
}
