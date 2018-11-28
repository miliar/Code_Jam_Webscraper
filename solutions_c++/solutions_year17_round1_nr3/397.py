#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <map>

using namespace std;

int hd, ad, hk, ak, b, d;

struct Node {
    int h1, h2, a1, a2;
    friend bool operator <(const Node& x, const Node& y) {
        auto t1 = make_pair(make_pair(x.h1, x.h2), make_pair(x.a1, x.a2));
        auto t2 = make_pair(make_pair(y.h1, y.h2), make_pair(y.a1, y.a2));
        return t1 < t2;
    }
};

int bfs() {
    map<Node, int> mp;
    mp[Node{hd, hk, ad, ak}] = 1;
    queue<Node> q;
    q.push(Node{hd, hk, ad, ak});

    int ans = -1;
    while (!q.empty()) {
        auto x = q.front(); q.pop;
        if (x.h1 == 0) break;
        q.push(x);
    }

    return ans;
}

int main(int argc, const char* argv[]) {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T; cin >> T;
    int kase = 1;
    while (T --) {

        cin >> hd >> ad >> hk >> ak >> b >> d;
        
        int ans = bfs();
        printf("Case #%d: ", kase ++);
        if (ans == -1) puts("IMPOSSIBLE");
        else cout<<ans - 1<<endl;
  }
  return 0;
}