
#include <iostream>
#include <string.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned ll
#define db double
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PII pair<int, int>

const string INPUT_FILE="input.txt";
const string OUTPUT_FILE="c.txt";

int t;
ll n,k;

void solve() {
    ll i=1;
    ll p=1;
    ll nn=n;
    while (k>i) {
        k-=i;
        if (nn%2==0) nn=nn/2-1;
        else nn/=2;
        i*=2;
    }
    ll rem=n-(i-1);
    ll y=rem-i*nn;
    if (k<=y) nn++;
    ll a=nn/2;
    ll b=nn%2==0?(nn/2-1):(nn/2);
    printf("%lld %lld\n",a,b);
}

int main() {

    freopen(INPUT_FILE.c_str(),"r",stdin);
    freopen(OUTPUT_FILE.c_str(),"w",stdout);

    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++) {
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",tt);
        solve();
    }
}