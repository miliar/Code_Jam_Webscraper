//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <unordered_set>
#include <stack>
#include <list>
#include <sstream>
#include <iomanip>
#include <complex>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a))
#define INF 0x3f3f3f3f
#define lINF 0x3f3f3f3f3f3f3f3fll
#define dINF 1e30
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define mp make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define cp complex<double>
#define here printf("!!!!!!!!\n");
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
#define upmin(a,b) {if ((a)>(b)) (a)=(b);}
#define upmax(a,b) {if ((a)<(b)) (a)=(b);}
#define upmod(a,b) (a)=((a)%(b)+(b))%(b)
#define equ(a,b) (fabs(a-b)<eps)
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;

#define maxn 11000

struct node {
    int k;
    int num;
    bool operator < (const node &I) const {
        return num > I.num || (num == I.num && k < I.k);
    }
};

int n;
int R, Y, B;
int O, G, V;
int a[6];
int st[maxn];

int pre() {
    if (a[0] > a[2] + a[4] || a[2] > a[0] + a[4] || a[4] > a[0] + a[2]) return 0;
    return 1;
}

int main() {
    int T, cas;
    freopen("B-small-attempt1.in", "r", stdin);
    //rin;
    pout;
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < 6; i++) scanf("%d", &a[i]);
        int flag = pre();
        if (flag == 0) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        
        for (int i = 0; i < n; i++) {
            node b[3];
            b[0].k = 0; b[0].num = a[0];
            b[1].k = 2; b[1].num = a[2];
            b[2].k = 4; b[2].num = a[4];
            sort(b, b + 3);

            for (int j = 0; j < 3; j++) {
                if (i > 0 && st[i - 1] == b[j].k) continue;
                st[i] = b[j].k;
                a[b[j].k]--;
                break;
            }

        }

        if (st[0] == st[n - 1]) swap(st[n - 2], st[n - 1]);
        printf("Case #%d: ", cas);
        for (int i = 0; i < n; i++) {
            if (st[i] == 0) putchar('R');
            if (st[i] == 1) putchar('O');
            if (st[i] == 2) putchar('Y');
            if (st[i] == 3) putchar('G');
            if (st[i] == 4) putchar('B');
            if (st[i] == 5) putchar('V');
        }
        printf("\n");
    }

    return 0;
}