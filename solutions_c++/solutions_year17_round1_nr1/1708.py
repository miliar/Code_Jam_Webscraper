#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

const int MAX = 30;
const int INF = INT_MAX/4;

string board[MAX];
int cases;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef FSOCIETY
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // FSOCIETY

    int t; cin >> t;
    while(t--) {
        int n, m; cin >> n >> m;
        for(int i = 0; i < n; i++) {
            cin >> board[i];
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(board[i][j] == '?') continue;
                int pos = j+1;
                while(pos < m && board[i][pos] == '?') {
                    board[i][pos] = board[i][j];
                    pos++;
                }
                pos = j-1;
                while(pos >= 0 && board[i][pos] == '?') {
                    board[i][pos] = board[i][j];
                    pos--;
                }
            }
        }


        cout << "Case #" << ++cases << ":\n";

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(board[i][j] == '?') continue;
                int pos = i+1;
                while(pos < n && board[pos][j] == '?') {
                    board[pos][j] = board[i][j];
                    pos++;
                }
                pos = i-1;
                while(pos >= 0 && board[pos][j] == '?') {
                    board[pos][j] = board[i][j];
                    pos--;
                }
                assert(board[i][j] != '?');
            }
//            cout << "\n";
        }

        for(int i = 0; i < n; i++) {
            cout << board[i] << "\n";
        }

    }

}
