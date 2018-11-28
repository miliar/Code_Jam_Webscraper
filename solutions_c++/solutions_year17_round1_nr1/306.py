#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define debug(x) cerr << #x << " = " << (x) << endl;
template<typename T>
ostream& operator<<(ostream& o, vector<T>& v) {
    for (auto& x : v) o << x << ' ';
    return o;
}
char grid[30][30];
void solve(){
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> grid[i][j];
    int noni = -1, nonj = -1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (grid[i][j] != '?') {
                noni = i;
                nonj = j;
                goto FIN;
            }
 FIN:;
    // fill in non
    grid[noni][0] = grid[noni][nonj];
    for (int j = 1; j < m; j++){
        if (grid[noni][j] != '?') continue;
        grid[noni][j] = grid[noni][j-1];
    }
    for (int i = noni - 1; i >= 0; i--){
        nonj = -1;
        for (int j = 0; j < m; j++)
            if (grid[i][j] != '?') {
                nonj = j;
                break;
            }
        if (nonj == -1) {
            for (int j = 0; j < m; j++)
                grid[i][j] = grid[i+1][j];
        } else {
            grid[i][0] = grid[i][nonj];
            for (int j = 1; j < m; j++){
                if (grid[i][j] != '?') continue;
                grid[i][j] = grid[i][j-1];
            }
        }
    }
    for (int i = noni+1; i < n; i++){
        nonj = -1;
        for (int j = 0; j < m; j++)
            if (grid[i][j] != '?') {
                nonj = j;
                break;
            }
        if (nonj == -1) {
            for (int j = 0; j < m; j++)
                grid[i][j] = grid[i-1][j];
        } else {
            grid[i][0] = grid[i][nonj];
            for (int j = 1; j < m; j++){
                if (grid[i][j] != '?') continue;
                grid[i][j] = grid[i][j-1];
            }
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cout << grid[i][j];
            assert(grid[i][j] != '?');
        }
        cout << endl;
    }
}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++) {
        cout << "Case #" << cs << ":" << endl;
        solve();
    }

}
