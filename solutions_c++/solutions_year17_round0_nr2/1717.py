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

#define maxn 1100

char st[maxn];
int n;

void process() {
    int flag = -1;
    for (int i = 0; i < n - 1; i++) {
        if (st[i] > st[i + 1]) flag = i;
    }
    if (flag == -1) return;
    for (int i = n - 2; i >= 0; i--) {
        if (st[i] > st[i + 1]) {
            st[i]--;
            for (int j = i + 1; j < n; j++)
                st[j] = '9';
        }
    }
   
}

int main() {
    int T, cas;
    freopen("B-large.in", "r", stdin);
    //rin;
    pout;
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++) {
        scanf("%s", st);
        n = strlen(st);
        process();
        printf("Case #%d: ", cas);
        if (st[0] != '0') printf("%c", st[0]);
        for (int i = 1; i < n; i++) {
            printf("%c", st[i]);
        }
        putchar('\n');
    }

    return 0;
}