#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 100;

int n, m;
char s[N][N];

void print() {
    for(int i = 0; i < n; ++i) cout << s[i] << endl;
}
bool is_shooter(char ch) {
    if (ch == '|' || ch == '-') {
        puts("IMPOSSIBLE");
        return true;
    }
    return false;
}
void check() {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            if (s[i][j] == '#') continue;
            int jj = j;
            while(jj + 1 < m && s[i][jj + 1] != '#') jj += 1;
            int cnt = 0;
            for(int cj = j; cj <= jj; ++cj) if(s[i][cj] == '-') cnt += 1;
            if (cnt > 1) {
                for(int cj = j; cj <= jj; ++cj) if(s[i][cj] == '-') s[i][cj] = '|';
            }
        }
    }    
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            if (s[i][j] == '-') {
                for(int jj = j - 1; jj >= 0 && s[i][jj] != '#'; --jj) {
                    if (s[i][jj] == '.') s[i][jj] = '$';
                    if (is_shooter(s[i][jj])) return;
                }
                for(int jj = j + 1; jj < m && s[i][jj] != '#'; ++jj) {
                    if (s[i][jj] == '.') s[i][jj] = '$';
                    if (is_shooter(s[i][jj])) return;                    
                }
            }
            else if(s[i][j] == '|') {
                for (int ii = i - 1; ii >= 0 && s[ii][j] != '#'; --ii) {
                    if (s[ii][j] == '.') s[ii][j] = '$';
                    if (is_shooter(s[ii][j])) return; 
                }
                for (int ii = i + 1; ii < n && s[ii][j] != '#'; ++ii) {
                    if (s[ii][j] == '.') s[ii][j] = '$';
                    if (is_shooter(s[ii][j])) return; 
                }
            }
        }
    }
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) if(s[i][j] == '.') {
            puts("IMPOSSIBLE");
            return;
        }
    }
    
    puts("POSSIBLE");
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) if(s[i][j] == '$') s[i][j] = '.';
    }
    print();
}
void _main() {
    cin >> n >> m;
    for(int i = 0; i < n; ++i) cin >> s[i];
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j) if(s[i][j] == '|') s[i][j] = '-';
    check();

}
int main() {
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}