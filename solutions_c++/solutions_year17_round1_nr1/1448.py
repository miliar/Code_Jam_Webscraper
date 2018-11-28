#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-large (1).in", "r", stdin);
    //freopen("A-large (1).out", "w", stdout);
    int T, R, C;
    cin >> T;

    char temp;
    char arr[100][100];

    for(int t = 0; t < T; t++){
        cin >> R >> C;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++)
            {
                cin >> arr[i][j];
            }
        }

        for(int i = 0; i < R; i++){
            for(int j = 1; j < C; j++)
            {
                if(arr[i][j] == '?'){
                    arr[i][j] = arr[i][j-1];
                }
            }
        }

        for(int i = 0; i < R; i++){
            for(int j = C-1; j > 0; j--)
            {
                if(arr[i][j-1] == '?'){
                    arr[i][j-1] = arr[i][j];
                }
            }
        }

        for(int i = 1; i < R; i++){
            for(int j = 0; j < C; j++)
            {
                if(arr[i][j] == '?'){
                    arr[i][j] = arr[i-1][j];
                }
            }
        }

        for(int i = R-1; i > 0; i--){
            for(int j = 0; j < C; j++)
            {
                if(arr[i-1][j] == '?'){
                    arr[i-1][j] = arr[i][j];
                }
            }
        }
        cout << "Case #" << t+1 << ":" << endl;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++)
            {
                cout << arr[i][j];
            }
            cout << endl;
        }
    }

    return 0;
}
