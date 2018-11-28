#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 2000;
int num[6]; // R, O, Y, G, B, V
int ans[N];
int t[N];
int n;
inline void Add(int& x, int y){
    x += y;
    if (x >= n) x -= n;
}
bool cmp(int p, int q){
    return num[p] < num[q];
}
bool solve1(){
    memset(ans, 0xff, sizeof(ans));
    int t[3] = {0, 2, 4};
    sort(t, t+3, cmp);
    if (num[t[2]] * 2 > n) return 0;
    int cur = 0;
    for (int i=0; i<num[t[2]]; i++){
        ans[cur] = t[2];
        Add(cur, 2);
    }
    if (ans[cur] != -1) Add(cur, 1);
    for (int i=0; i<num[t[1]]; i++){
        ans[cur] = t[1];
        Add(cur, 2);
        if (ans[cur] != -1) Add(cur, 1);
    }
    for (int i=0; i<n; i++) if (ans[i] == -1)
        ans[i] = t[0];
    return 1;
}
int main(){
    int exc[6];
    exc[0] = 'R';
    exc[1] = 'O';
    exc[2] = 'Y';
    exc[3] = 'G';
    exc[4] = 'B';
    exc[5] = 'V';
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%d", &n);
        for (int i=0; i<6; i++) scanf("%d", &num[i]);
        if (!num[1] && !num[3] && !num[5]){
            if (!solve1()) printf("Case #%d: IMPOSSIBLE\n", cas);
            else {
                printf("Case #%d: ", cas);
                for (int i=0; i<n; i++) putchar(exc[ans[i]]);
                puts("");
            }
        } else {

        }
    }
    fclose(stdout);
    return 0;
}

