#include <iostream>
#include <set>
using namespace std;

const int INF = 1000000000;

struct node {
    int a, b, c, d;
    int ans;
    node() {}
    node(int _a, int _b, int _c, int _d, int _ans): a(_a), b(_b), c(_c), d(_d), ans(_ans) {}
    bool operator < (const node &B) const {
        if (ans != B.ans) return ans < B.ans;
        if (a != B.a) return a < B.a;
        if (b != B.b) return b < B.b;
        if (c != B.c) return c < B.c;
        return d < B.d;
    }
};

int HD, AD, HK, AK, B, D;
int f[101][101][101][101];
bool z[101][101][101][101];

void update(int &a, int b) {
    if (a == -1 || a > b) a = b;
}

int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cin >> HD >> AD >> HK >> AK >> B >> D;
        cout << "Case #" << times << ": ";
        /*
        if (HD <= AK) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        */
        memset(f, -1, sizeof(f));
        memset(z, 0, sizeof(z));
        int ans = INF;
        set<node> S;
        S.insert(node(HD, AD, HK, AK, 0));
        f[HD][AD][HK][AK] = 0;
        while (!S.empty()) {
            node temp = *S.begin();
            S.erase(S.begin());
            int a = temp.a, b = temp.b, c = temp.c, d = temp.d;
            if (z[a][b][c][d]) continue;
            temp.ans = f[a][b][c][d];
           // cout << a << " " << b << " " << c << " " << d << " " << temp.ans << endl;
            z[a][b][c][d] = true;
            if (c == 0) {
            //    cout << a << " " << b << " " << c << " " << d << " " << temp.ans << " " << ans << endl;
                ans = min(ans, temp.ans);
                continue;
            }

            if (HD > d) {
                update(f[HD - d][b][c][d], temp.ans + 1);
                S.insert(node(HD - d, b, c, d, temp.ans + 1));
            }
            int tp = max(0, d - D);
            if (a > tp) {
                update(f[a - tp][b][c][tp], temp.ans + 1);
                S.insert(node(a - tp, b, c, tp, temp.ans + 1));
            }
            if (b >= c) {
                update(f[a][b][0][d], temp.ans + 1);
                S.insert(node(a, b, 0, d, temp.ans + 1));
            }
            if (a > d) {
                tp = min(b + B, 100);
                update(f[a - d][tp][c][d], temp.ans + 1);
                S.insert(node(a - d, tp, c, d, temp.ans + 1));
                if (c > b) {
                    update(f[a - d][b][c - b][d], temp.ans + 1);
                    S.insert(node(a - d, b, c - b, d, temp.ans + 1));
                }
            } 
        }

        if (ans == INF) cout << "IMPOSSIBLE" << endl; else cout << ans << endl;
    }
    return 0;
}