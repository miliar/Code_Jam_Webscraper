#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
//#define LL "%lld"
#define RLL(x) scanf(LL,&(x))


void test(int T)
{
    ll n,k;
    cin>>n>>k;
    ll d = 1;
    while(d < k)
    {
        n -= d;
        k -= d;
        d <<= 1;
    }
    ll last = n / d + (n % d >= k);
    printf("Case #%d: %lld %lld\n", T, last / 2, (last - 1) / 2);
    
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/c.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/c.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
