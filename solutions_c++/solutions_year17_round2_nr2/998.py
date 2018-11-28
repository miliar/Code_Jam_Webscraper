#define DEBUG
#define TXTOUT
#include<bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const double EPS = 1e-8;
const int M = 1e3 + 10;
int n, r, o, y, g, b, v;
char answer[M];
struct Node {
    char type;
    int number;
    Node() {}
    Node(char _t, int _n) {
        type = _t;
        number = _n;
    }
    bool operator < (const Node &b) const {
        return number > b.number;
    }
};
vector<Node> a;
void Solve() {
    a.clear();
    a.push_back(Node('R', r));
    a.push_back(Node('Y', y));
    a.push_back(Node('B', b));
    sort(a.begin(), a.end());
    int now = 0;
    for (int i = 0; i < n; i += 2) {
        if (a[now].number == 0) now++;
        answer[i] = a[now].type;
        a[now].number--;
    }
    for (int i = 1; i < n; i += 2) {
        if (a[now].number == 0) now++;
        answer[i] = a[now].type;
        a[now].number--;
    }
    answer[n] = '\0';
    for (int i = 0; i < n; i++) {
        if (answer[i] == answer[(i + 1) % n]) {
            strcpy(answer, "IMPOSSIBLE");
            return ;
        }
    }
}
int main() {
    #ifdef TXTOUT
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    #endif // TXTOUT
    int t, cas = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        Solve();
        printf("Case #%d: %s\n", cas++, answer);
    }
    return 0;
}
