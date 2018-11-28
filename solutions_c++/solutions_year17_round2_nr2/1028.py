#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())
#define For(i, a, b) for(int i = a;i <= b; ++i)
#define fi first
#define se second

template <typename T>
inline ostream &operator << (ostream &out, const vector <T> &v) {
    for(auto to: v)
        out << to << ' ';
    out << '\n';
    return out;
}

template <typename T>
inline ostream &operator << (ostream &out, const set <T> &v) {
    for(auto to: v)
        out << to << ' ';
    out << '\n';
    return out;
}


typedef pair <int,int> pii;
typedef long long i64;

const i64 INF = 1e18 + 9;

int main()
{
#ifdef HOME
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // HOME
    ios::sync_with_stdio(NULL); cin.tie(NULL);
    int T; cin >> T;
    For(t, 1, T) {
        cout << "Case #" << t << ": ";
        int n; cin >> n;
        int red, red_yellow, yellow, yellow_blue, blue, red_blue;
        cin >> red >> red_yellow >> yellow >> yellow_blue >> blue >> red_blue;

        vector <int> color (4);
        color[1] = red, color[2] = yellow, color[3] = blue;

        vector <int> res;

        bool good = true;
        For(i, 1, n) {

            int choose = -1;
            for(int j = 1;j <= 3; ++j) {
                if(!res.empty() && j == res[sz(res) - 1])
                    continue;

                if(i == n && j == res[0])
                    continue;
                if(choose == -1) {
                    choose = j;
                    continue;
                }
                if(color[j] > color[choose] || (color[j] == color[choose] && (!res.empty() && res[0] == j)))
                    choose = j;
            }
            if(choose == -1 || color[choose] == 0) {
                good = false;
                break;
            }
            res.push_back(choose);
            color[choose]--;
        }

        if(!good) {
            cout << "IMPOSSIBLE" << '\n';
            continue;
        }

        vector <char> go = {'x', 'R', 'Y', 'B'};
        for(auto to: res) {
            cout << go[to];
        }
        cout << '\n';
    }
    return 0;
}
