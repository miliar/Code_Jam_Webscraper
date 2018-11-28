
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define de(x) cout << #x << "=" << x << endl

int l[3],r[3],a[5];

int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("xx.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);

        ///
        int n,m;scanf("%d%d",&n,&m);

        ///read
        for(int i=1;i<=n+m;++i) scanf("%d%d",l+i,r+i);

        ///
        if(n>m) swap(n,m);

        ///
        if(m==1) {
            puts("2");
            continue;
        }

        ///
        if(l[1]>l[2]) {
            swap(l[1],l[2]);
            swap(r[1],r[2]);
        }

        a[1]=l[1]+1440-r[2];a[2]=l[2]-r[1];

        ///solve
        if(max(a[1],a[2])>=720) puts("2");
        else puts("4");


    }
    return 0;
}
