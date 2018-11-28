#include <iostream>
#include <string>
using namespace std;
#define MAX 26
int matrix[MAX][MAX];
void solve(){
    int T, t, R, C, i, j, k;
    string line;
    cin >> T;
    for(t = 1; t <= T; t++){
        cin >> R >> C;
        for(i = 0; i < R; i++){
            cin >> line;
            for(j = 0; j < C; j++){
                if(line[j] == '?')
                    matrix[i][j] = -1;
                else
                    matrix[i][j] = line[j] - 'A';
            }
        }
        for(i = 0; i < R; i++){
            for(j = 0; j < C; j++){
                if(matrix[i][j] == -1)
                    continue;
                k = j + 1;
                while(k < C && matrix[i][k] == -1)
                    matrix[i][k++] = matrix[i][j];
                k = j - 1;
                while(k >= 0 && matrix[i][k] == -1)
                    matrix[i][k--] = matrix[i][j];
            }
        }
        for(j = 0; j < C; j++){
            for(i = 0; i < R; i++){
                if(matrix[i][j] == -1)
                    continue;
                k = i + 1;
                while(k < R && matrix[k][j] == -1)
                    matrix[k++][j] = matrix[i][j];
                k = i - 1;
                while(k >= 0 && matrix[k][j] == -1)
                    matrix[k--][j] = matrix[i][j];
            }
        }
        cout << "Case #" << t << ":" << endl;
        for(i = 0; i < R; i++){
            for(j = 0; j < C; j++){
                cout << char(matrix[i][j] + 'A');
            }
            cout << endl;
        }
    }

}

int main(){
    solve();
    return 0;
}
