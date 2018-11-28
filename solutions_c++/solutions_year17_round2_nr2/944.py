#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>
#include <set>
#include <cmath>

using namespace std;

int N, R, O, Y, G, B, V;

int ALL;

string fill(int A, int B, int C, string a, string b, string c) {
    string ret = "";
    int k = C - A + B;
    while (k --) {
        ret += a;
        ret += b;
        ret += c;
    }
    k = A - C;
    while (k --) {
        ret += a;
        ret += b;
    }
    k = A - B;
    while (k --) {
        ret += a;
        ret += c;
    }
    return ret;
}

string make_ring(int Y, int B, int R) {
    /*
    for (int i = 0; i < ALL; ++ i)
        ring.push_back(' ');
    */
    if (Y >= B && Y >= R) {
        if (B >= R) {
            return fill(Y, B, R, "Y", "B", "R");
        }
        else {
            return fill(Y, R, B, "Y", "R", "B");
        }
    }
    else if (R >= Y && R >= B) {
        if (Y >= B) {
            return fill(R, Y, B, "R", "Y", "B");
        }
        else {
            return fill(R, B, Y, "R", "B", "Y");
        }
    }
    if (B >= Y && B >= R) {
        if (Y >= R) {
            return fill(B, Y, R, "B", "Y", "R");
        }
        else {
            return fill(B, R, Y, "B", "R", "Y");
        }
    }

}

bool fml(char a, char b) {
    if (a == 'R') {
        if (b == 'R' || b == 'V' || b == 'O') return false;
        return true;
    }
    if (a == 'Y') {
        if (b == 'Y' || b == 'O' || b == 'G') return false;
        return true;
    }
    if (a == 'B') {
        if (b == 'B' || b == 'G' || b == 'V') return false;
        return true;
    }
    if (a == 'V') {
        if (b == 'V' || b == 'B' || b == 'R') return false;
        return true;
    }
    if (a == 'O') {
        if (b == 'O' || b == 'R' || b == 'Y') return false;
        return true;
    }
    if (a == 'G') {
        if (b == 'G' || b == 'Y' || b == 'B') return false;
        return true;
    }
}

bool checker(const vector<char> &ring) {
    for (int i = 0; i < N; ++ i) {
        if (!fml(ring[i], ring[(i + 1) % N])) return false;
        if (!fml(ring[i], ring[(i - 1 + N) % N])) return false;
    }
    return true;
}

bool checker(string &ring) {
    for (int i = 0; i < N; ++ i) {
        if (!fml(ring[i], ring[(i + 1) % N])) return false;
        if (!fml(ring[i], ring[(i - 1 + N) % N])) return false;
    }
    return true;
}

string check() {
    vector<char> ring;
    for (int i = 0; i < R; ++ i)
        ring.push_back('R');
    for (int i = 0; i < O; ++ i)
        ring.push_back('O');
    for (int i = 0; i < Y; ++ i)
        ring.push_back('Y');
    for (int i = 0; i < G; ++ i)
        ring.push_back('G');
    for (int i = 0; i < B; ++ i)
        ring.push_back('B');
    for (int i = 0; i < V; ++ i)
        ring.push_back('V');
    sort(ring.begin(), ring.end());
    do {
        if (checker(ring)) {
            string ret = "";
            for (int i = 0; i < ring.size(); ++ i)
                ret += ring[i];
            return ret;
        }
    } while (next_permutation(ring.begin(), ring.end()));
    return "IMPOSSIBLE";
}

string solve() {
    if (N < 4) {
        if (N == 1) {
            if (R == 1) return "R";
            if (O == 1) return "O";
            if (Y == 1) return "Y";
            if (G == 1) return "G";
            if (B == 1) return "B";
            if (V == 1) return "V";
        }
        return check();
    }

    if (V != 0 && V == Y) {
        if (V + Y == N) {
            string ans = "";
            for (int i = 0; i < V; ++ i)
                ans += "VY";
            return ans;
        }
        return "IMPOSSIBLE";
    }
    if (G != 0 && R == G) {
        if (R + G == N) {
            string ans = "";
            for (int i = 0; i < R; ++ i)
                ans += "RG";
            return ans;
        }
        return "IMPOSSIBLE";
    }
    if (O != 0 && B == O) {
        if (B + O == N) {
            string ans = "";
            for (int i = 0; i < B; ++ i)
                ans += "BO";
            return ans;
        }
        return "IMPOSSIBLE";
    }

    Y -= V;
    if (V != 0 && Y < 1) return "IMPOSSIBLE";
    B -= O;
    if (O != 0 && B < 1) return "IMPOSSIBLE";
    R -= G;
    if (G != 0 && R < 1) return "IMPOSSIBLE";


    if (Y > R + B || B > Y + R || R > B + Y) return "IMPOSSIBLE";


    ALL = Y + B + R;
    /*
    cout << "Y = " << Y << endl;
    cout << "B = " << B << endl;
    cout << "R = " << R << endl;
    */
    //cout << ALL << endl;
    string ring = make_ring(Y, B, R);
    string ans = "";
    for (int i = 0; i < ALL; ++ i)
        if (ring[i] == 'Y') {
            while (V > 0) {
                ans += "YV";
                -- V;
            }
            ans += "Y";
        }
        else if (ring[i] == 'B') {
            while (O > 0) {
                ans += "BO";
                -- O;
            }
            ans += "B";
        }
        else if (ring[i] == 'R') {
            while (G > 0) {
                ans += "RG";
                -- G;
            }
            ans += "R";
        }
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++ test) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        printf("Case #%d: ", test);
        string ans = solve();
        cout << ans << endl;
        /*
        if (ans != "IMPOSSIBLE")
            cout << checker(ans) << endl;
        else
            cout << "IMPOSSIBLE" << endl;
        */
        //cout << solve() << endl;
    }
    return 0;
}
