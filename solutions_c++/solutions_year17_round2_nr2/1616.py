#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>
#pragma warning(disable : 4244)
#pragma warning(disable : 4267)
#pragma warning(disable : 4305)
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
#define INF 18000000000000000
#define F_INF 1e100

int N, R, O, Y, G, B, V;
int i;

struct Value {
    string S;
    int R, O, Y, G, B, V;
    Value() : S(""), R(0), O(0), Y(0), G(0), B(0), V(0) {}
};

string solve(string ans, int N, int R, int O, int Y, int G, int B, int V) {
    --N;
    while (N > 0) {
        //cout << ans << endl;
        char c = ans[ans.length() - 1];
        if (c == 'R') {
            int M = max(Y, max(G, B));
            if (M == 0) return "IMPOSSIBLE";
            if (Y == M) {
                ans += "Y"; --Y;
            }
            else if (G == M) {
                ans += "G"; --G;
            }
            else if (B == M) {
                ans += "B"; --B;
            }
        }
        else if (c == 'Y') {
            int M = max(R, max(V, B));
            if (M == 0) return "IMPOSSIBLE";
            if (R == M) {
                ans += "R"; --R;
            }
            else if (V == M) {
                ans += "V"; --V;
            }
            else if (B == M) {
                ans += "B"; --B;
            }
        }
        else if (c == 'B') {
            int M = max(R, max(Y, max(O, G)));
            if (M == 0) return "IMPOSSIBLE";
            if (R == M) {
                ans += "R"; --R;
            }
            else if (Y == M) {
                ans += "Y"; --Y;
            }
            else if (O == M) {
                ans += "O"; --O;
            }
            else if (G == M) {
                ans += "G"; --G;
            }
        }
        else if (c == 'G') {
            int M = max(R, B);
            if (M == 0) return "IMPOSSIBLE";
            if (R == M) {
                ans += "R"; --R;
            }
            else if (B == M) {
                ans += "B"; --B;
            }
        }
        else if (c == 'V') {
            int M = max(Y, O);
            if (M == 0) return "IMPOSSIBLE";
            if (Y == M) {
                ans += "Y"; --Y;
            }
            else if (O == M) {
                ans += "O"; --O;
            }
        }
        else if (c == 'O') {
            int M = max(V, B);
            if (M == 0) return "IMPOSSIBLE";
            if (V == M) {
                ans += "V"; --V;
            }
            else if (B == M) {
                ans += "B"; --B;
            }
        }
        --N;
    }

    //cout << ans << endl;
    char c1 = ans[0], c2 = ans[ans.length() - 1];
    if (c1 == c2) return "IMPOSSIBLE";

    switch (c1) {
    case 'R':
        if (c2 == 'V' || c2 == 'O') return "IMPOSSIBLE";
        break;
    case 'Y':
        if (c2 == 'O' || c2 == 'G') return "IMPOSSIBLE";
        break;
    case 'B':
        if (c2 == 'V') return "IMPOSSIBLE";
        break;
    case 'G':
        if (c2 == 'R' || c2 == 'B') return ans;
        break;
    case 'V':
        if (c2 == 'Y' || c2 == 'O') return ans;
        break;
    case 'O':
        if (c2 == 'V' || c2 == 'B') return ans;
        break;
    }
    return ans;
}

string F() {
    string a = "IMPOSSIBLE";
    if (R > 0) a = solve("R", N, R-1, O, Y, G, B, V);
    if (a != "IMPOSSIBLE") return a;
    if (O > 0) a = solve("O", N, R, O-1, Y, G, B, V);
    if (a != "IMPOSSIBLE") return a;
    if (Y > 0) a = solve("Y", N, R, O, Y-1, G, B, V);
    if (a != "IMPOSSIBLE") return a;
    if (G > 0) a = solve("G", N, R, O, Y, G-1, B, V);
    if (a != "IMPOSSIBLE") return a;
    if (B > 0) a = solve("B", N, R, O, Y, G, B-1, V);
    if (a != "IMPOSSIBLE") return a;
    if (V > 0) a = solve("V", N, R, O, Y, G, B, V-1);
    return a;
}

int main() {
    int T;  cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> R >> O >> Y >> G >> B >> V;

        cout << "Case #" << t << ": " << F() << endl;
    }
    return 0;
}

