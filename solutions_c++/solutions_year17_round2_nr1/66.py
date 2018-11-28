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
//#define LL "%I64d"
#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

void test(int T)
{
    ll n,d;
    cin>>d>>n;
    double maxt = 0;
    for(int i = 0; i < n; ++i)
    {
        int k,s;
        scanf("%d%d",&k,&s);
        maxt = max(maxt, (d-k)/double(s));
    }
    double res = d / maxt;
    printf("Case #%d: %.10lf\n", T, res);
    
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/a.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/a.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
