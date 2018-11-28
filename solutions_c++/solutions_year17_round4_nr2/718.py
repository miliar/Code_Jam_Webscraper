#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <bitset>
#include <cstdlib>
#include <cmath>
#include <set>
#include <list>
#include <deque>
#include <map>
#include <queue>
#include <fstream>
#include <cassert>
#include <cmath>
#include <sstream>
#include <time.h>
#include <complex>
#include <iomanip>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<double,double> dd;
typedef pair<char,char> cc;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> l4;
const double eps = 0.005;
const int maxn = 2010;
const ll mod = 1e9+7;

int T,n,c,m;
int t1,t2;
int a[3];
int in[1010];
int in2[1010];
vi G[maxn];
int check[maxn];
int matching[maxn];
int tot1;
int tot2;
bool dfs(int u)
{
    for (auto i : G[u]) { // 对 u 的每个邻接点
        int v = i;
        if (!check[v]) {     // 要求不在交替路中
            check[v] = true; // 放入交替路
            if (matching[v] == -1 || dfs(matching[v])) {
                // 如果是未盖点，说明交替路为增广路，则交换路径，并返回成功
                matching[v] = u;
                matching[u] = v;
                return true;
            }
        }
    }
    return false; // 不存在增广路，返回失败
}

int hungarian()
{
    int ans = 0;
    memset(matching, -1, sizeof(matching));
    for (int u=0; u < tot1; ++u) {
        if (matching[u] == -1) {
            memset(check, 0, sizeof(check));
            if (dfs(u))
                ++ans;
        }
    }
    return ans;
}

int main() {
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        tot1 = tot2 = 0;
        scanf("%d%d%d",&n,&c,&m);
        memset(in, 0, sizeof(in));
        memset(in2, 0, sizeof(in2));
        memset(a, 0, sizeof(a));
        for (int i = 0; i < m; i++) {
            scanf("%d%d",&t1,&t2);
            a[t2]++;
            if (t2 == 1) {
                in[tot1++] = t1;
            } else {
                in2[tot2++] = t1;
            }
        }
        sort(in,in+tot1);
        sort(in2,in2+tot2);
        for (int i = 0; i< maxn; i++) {
            G[i].clear();
        }
        for (int i = 0; i < tot1; i++) {
            for (int j = 0; j < tot2; j++) {
                if (in[i] != in2[j]) {
                    G[i].push_back(j+1000);
                    G[j+1000].push_back(i);
                }
            }
        }
        int ans2 = hungarian();
        int num1 = 0;
        int num2 = 0;
        for (int i = 0; i < tot1; i++) {
            if (matching[i] == -1 && in[i] == 1) {
                num1++;
            }
        }
        for (int i = 0; i < tot2; i++) {
            if (matching[i+1000] == -1 && in2[i+1000] == 1) {
                num2++;
            }
        }
        if (num1 || num2) {
            printf("%d 0\n",ans2+tot1-ans2+tot2-ans2);
        } else {
            printf("%d %d\n",max(tot1,tot2),min(tot1,tot2)-ans2);
        }
    }
}




