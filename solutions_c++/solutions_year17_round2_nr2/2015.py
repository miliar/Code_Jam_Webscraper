#include <string>
#include <fstream>
using namespace std;
int N, R, O, Y, G, B, V;

string solve() {
    int     r = R - G;
    int     y = Y - V;
    int     b = B - O;
    string  S(r + y + b, '?');
    
    if (r)      { S[0] = 'R'; r--; }
    else if (y) { S[0] = 'Y'; y--; }
    else if (b) { S[0] = 'B'; b--; }
    
    for (int i = 0; r + y + b; i++) {
        switch (S[i]) {
            case 'R':
                if (y + b == 0) return "IMPOSSIBLE";
                if (y > b) { S[i+1] = 'Y'; y--; } else { S[i+1] = 'B'; b--; }
                break;
            case 'Y':
                if (r + b == 0) return "IMPOSSIBLE";
                if (r > b) { S[i+1] = 'R'; r--; } else { S[i+1] = 'B'; b--; }
                break;
            case 'B':
                if (y + r == 0) return "IMPOSSIBLE";
                if (y > r) { S[i+1] = 'Y'; y--; } else { S[i+1] = 'R'; r--; }
                break;
        }
    }
    
    string ans = "";
    for (char c : S) {
        if (c == 'R') { if (G) { ans += "RGR"; G--; } else ans += "R"; }
        if (c == 'Y') { if (V) { ans += "YVY"; V--; } else ans += "Y"; }
        if (c == 'B') { if (O) { ans += "BOB"; O--; } else ans += "B"; }
    }
    
    while (G--) ans += "GR";
    while (V--) ans += "VY";
    while (O--) ans += "OB";
    
    for (int i = 0; i < ans.length(); i++)
        if (ans[i] == ans[(i + 1) % ans.length()]) return "IMPOSSIBLE";
    
    return ans;
}

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        f >> N >> R >> O >> Y >> G >> B >> V;
        string ans = solve();
        g << "Case #" << test << ": " << ans << endl;
    }
    
    return 0;
}
