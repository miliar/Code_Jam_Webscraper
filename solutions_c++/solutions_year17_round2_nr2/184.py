#include <bits/stdc++.h>

using namespace std;

pair<bool, string> solve_simple(int _R, int _B, int _Y)
{
    vector<pair<int, char>> t;
    t.push_back({_R, 'R'});
    t.push_back({_B, 'B'});
    t.push_back({_Y, 'Y'});

    sort(t.begin(), t.end());

    int R = t[0].first;
    char Rc = t[0].second;

    int B = t[2].first;
    char Bc = t[2].second;

    int G = t[1].first;
    char Gc = t[1].second;

    stringstream s;
    while (R and B > G) {
        s << Rc << Bc << Gc << Bc;
        R--, B--, G--, B--;
    }
    while (R) {
        s << Rc << Gc << Bc;
        R--; G--; B--;
    }
    while (G and B) {
        s << Gc << Bc;
        G--; B--;
    }
    if (G or B) {
        return {false, string()};
    } else {
        return {true, s.str()};
    }
}

void solve(int test_num)
{
    int n, _R, _O, _Y, _G, _B, _V;
    cin >> n >> _R >> _O >> _Y >> _G >> _B >> _V;

    string imp = " IMPOSSIBLE\n";

    if (_O == 0 and _G == 0 and _V == 0) {
        pair<bool, string> res = solve_simple(_R, _B, _Y);
        if (res.first) {
            cout << " " << res.second << '\n';
        } else {
            cout << imp;
        }
        return;
    } else {
        if (_B < _O) {
            cout << imp;
            return;
        }
        _B -= _O;
        if (_B == 0 and _O) {
            if (2 * _O == n) {
                string formed;
                for (int i = 0; i < _O; i++) {
                    formed.push_back('O');
                    formed.push_back('B');
                }
                cout << " " << formed << '\n';
                return;
            } else {
                cout << imp;
                return;
            }
        }

        if (_R < _G) {
            cout << imp;
            return;
        }
        _R -= _G;
        if (_R == 0 and _G) {
            if (2 * _G == n) {
                string formed;
                for (int i = 0; i < _G; i++) {
                    formed.push_back('G');
                    formed.push_back('R');
                }
                cout << " " << formed << '\n';
                return;
            } else {
                cout << imp;
                return;
            }
        }

        if (_Y < _V) {
            cout << imp;
            return;
        }
        _Y -= _V;
        if (_Y == 0 and _V) {
            if (2 * _V == n) {
                string formed;
                for (int i = 0; i < _V; i++) {
                    formed.push_back('V');
                    formed.push_back('Y');
                }
                cout << " " << formed << '\n';
                return;
            } else {
                cout << imp;
                return;
            }
        }

        pair<bool, string> res = solve_simple(_R, _B, _Y);
        if (not res.first) {
            cout << imp;
            return;
        }

        string result = res.second;
        if (_O) {
            string formed;
            for (int i = 0; i < _O; i++) {
                formed.push_back('O');
                formed.push_back('B');
            }
            result.insert(
                result.find("B") + 1,
                formed
            );
        }
        if (_G) {
            string formed;
            for (int i = 0; i < _G; i++) {
                formed.push_back('G');
                formed.push_back('R');
            }

            result.insert(
                result.find("R") + 1,
                formed
            );
        }
        if (_V) {
            string formed;
            for (int i = 0; i < _V; i++) {
                formed.push_back('V');
                formed.push_back('Y');
            }
            result.insert(
                result.find("Y") + 1,
                formed
            );
        }

        cout << " " << result << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    cout.setf(ios::fixed);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ":";
        solve(i);
    }
}
