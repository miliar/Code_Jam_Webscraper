#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

#define MAX 150
int health, attack, knight_h, knight_at;
int B, D;
bool met[MAX][MAX][MAX][MAX];

struct Node {
    int h, a, kh, ka;
    int dist;
    Node (int h, int a, int kh, int ka, int dist) : h(h), a(a), kh(kh), ka(ka), dist(dist) {}
    bool operator < (const Node& other) const {
        return dist > other.dist;
    }
};

lli dijkstra() {
        memset(met, false, sizeof(met));

        priority_queue<Node> q;
        q.push(Node(health, attack, knight_h, knight_at, 0));

        while (q.size()) {
            Node p = q.top();
            q.pop();

            if (p.a > 150) continue;

            if (p.kh <= 0)
                return p.dist;


            int ph = p.h;
            if (p.dist != 0)
                ph = p.h - p.ka;


            if (ph <= 0) continue;

            if (!met[p.h][p.a][p.kh][p.ka]) {
                met[p.h][p.a][p.kh][p.ka] = true;

                q.push(Node(ph, p.a, p.kh - p.a, p.ka, p.dist + 1));

                q.push(Node(ph, p.a + B, p.kh, p.ka, p.dist + 1));

                q.push(Node(health, p.a, p.kh, p.ka, p.dist + 1));
                int power_ = max(0, p.ka - D);
                q.push(Node(ph, p.a, p.kh, power_, p.dist + 1));
            }
        }
        return -1;
    }


int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {

        cin >> health >> attack >> knight_h >> knight_at;
        cin >> B >> D;

        int ans = dijkstra();

        cout << "Case #" << t << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
        cerr << t << "\n";
    }

    return 0;
}