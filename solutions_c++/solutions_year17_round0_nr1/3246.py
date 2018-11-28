#include <bits/stdc++.h>
using namespace std;
#define prt(k) cout<<#k" = "<<k<<"   ";
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int MAXN = 1701000 ;
const int INF = 0x3f3f3f3f;
int  n, k;
bool vis[MAXN];
int mask[323];
int ans[2334];
int f(string s)
{
    n = s.size();
    int ret = 0;
    for (int i=0;i<n;i++) if (s[i]=='+') ret=ret | (1<<i);
    return ret;
}
string toS(int mask)
{
    string s(n, '-');
    for (int i=0;i<n;i++) if(mask >> i & 1){
        s[i] = '+';
    }
    return s;
}
void BFS()
{
    memset(vis, 0, sizeof vis) ;
    vis[(1<<n)-1] = true;
    queue<pair<int, int> > Q;
    int cnt = 0;
    Q.push(make_pair((1<<n)-1, 0)); cnt ++;
    ans[(1<<n)-1] = 0;
    while (!Q.empty()) {
        int u = Q.front().first;
        int step = Q.front().second + 1;
        Q.pop();
        for (int pos = 0; pos + k - 1 < n; pos ++) {
            int v = u ^ mask[pos];
            if (!vis[v]) {
                Q.push(make_pair(v,step)); cnt++;
                ans[v] = step;
                vis[v] = true;
            }
        }
    }
//    printf("n = %d  k = %d  cnt = %d\n", n, k, cnt);
}
int main()
{

    int re ,ca = 1;
    cin >> re;
    while (re--) {
        string s;
        memset(ans, 63, sizeof ans);
        cin >> s >> k;
        int tar = f(s);
        memset(mask, 0, sizeof mask);
        for (int pos = 0; pos + k - 1 < n; pos ++)
        {
            for (int i=pos;i<pos+k;i++) {
                mask[pos] |= (1<<i);
            }
        }
        BFS();
        printf("Case #%d: ", ca++);
        if (ans[tar]==INF) puts("IMPOSSIBLE");
        else printf("%d\n", ans[tar]);
    }
    return 0;
}
