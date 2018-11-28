#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"
#define cv(c) (int)(c-'a')
#define db(x) cerr << #x << ": " << x << " "
#define db2(x, y) cerr << #x << ": " << x << " " << #y << ": " << y << " "
#define bn() cerr << endl
#define sep() cerr << "-------" << endl
#define inf 1000000002
#define linf 1000000000000000002

using namespace std;
typedef long long ll;
typedef long double ld;

string s[100];
vector<pair<int, int> > v;
int main(){
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("ou", "w", stdout);
    int t;
    cin >> t;
    int caso = 1;
    while (t--){
        int n, m;
        cin >> n >> m;
        v.clear();
        for (int i = 0; i < n; i++){
            cin >> s[i];
            for (int j = 0; j < m; j++){
                if (s[i][j] != '?'){
                    v.pb(mp(j, i));
                }
            }
        }
        sort(v.begin(), v.end());
        int ux = -1;
        for (int i = 0; i < v.size(); i++){
            int x = v[i].fi, y = v[i].se;
            char c = s[y][x];
            for (int j = y; j >= 0 && (s[j][x] == '?' || s[j][x] == c); j--){
                s[j][x] = c;
            }
            for (int j = y; j < n && (s[j][x] == '?' || s[j][x] == c); j++){
                s[j][x] = c;
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (s[i][j] == '?') continue;
                char c = s[i][j];
                for (int k = j; k >= 0 && (s[i][k] == '?' || s[i][k] == c); k--){
                    s[i][k] = c;
                }
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = m - 1; j >= 0; j--){
                if (s[i][j] == '?') continue;
                char c = s[i][j];
                for (int k = j; k < m && (s[i][k] == '?' || s[i][k] == c); k++){
                    s[i][k] = c;
                }
                break;
            }
        }
        cout << "Case #" << caso << ":" << endl;
        for (int i = 0; i < n; i++){
            cout << s[i] << endl;
        }
        caso++;
    }

    return 0;
}

