#include <bits/stdc++.h>

using namespace std;

int const N = 105;
char a[N][N];
int R, C;

void BFS(int x, int y){
    int u = x;
    while(a[u-1][y] == '?' && u > 1){
        a[u-1][y] = a[x][y];
        u--;
    }
    u = x;
    while(a[u+1][y] == '?' && u < R){
        a[u+1][y] = a[x][y];
        u++;
    }
}

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": " << endl;
        cin >> R >> C;
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                cin >> a[i][j];
            }
        }

        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                if(a[i][j] != '?') BFS(i, j);
            }
        }

        for(int i=1; i<=R; i++){
            for(int j=2; j<=C; j++){
                if(a[i][j] == '?'){
                    a[i][j] = a[i][j-1];
                }
            }
        }

        for(int i=1; i<=R; i++){
            for(int j=C-1; j>=1; j--){
                if(a[i][j] == '?'){
                    a[i][j] = a[i][j+1];
                }
            }
        }

        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                cout << a[i][j];
            }
            cout << endl;
        }

    }
}
