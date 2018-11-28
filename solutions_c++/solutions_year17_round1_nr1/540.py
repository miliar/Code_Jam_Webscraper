#include <bits/stdc++.h>

using namespace std;

int n,m,k,l,p,q;
int r,col;
int t;

char arr[27][27];
int heights[27];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> r >> col;
        for (int i = 0; i < r; i++){
            bool b = 0;
            char c = '*';
            for (int j = 0; j < col; j++){
                cin >> arr[i][j];
                if (!b && arr[i][j] != '?'){
                    b=1;
                    c=arr[i][j];
                    for (int k = j - 1; k >= 0; k--){
                        arr[i][k] = c;
                    }
                }
                else if (b && arr[i][j] != '?'){
                    c = arr[i][j];
                }
                else if (b && arr[i][j] == '?'){
                    arr[i][j] = c;
                }
            }
        }
        for (int j = 0; j < col; j++){
            bool b = 0;
            char c = '*';
            for (int i = 0; i < r; i++){
                if (!b && arr[i][j] != '?'){
                    b=1;
                    c=arr[i][j];
                    for (int k = i-1; k >= 0; k--){
                        arr[k][j]=c;
                    }
                }
                else if (b && arr[i][j] != '?'){
                    c = arr[i][j];
                }
                else if (b && arr[i][j] == '?'){
                    arr[i][j]=c;
                }
            }
        }

        cout << "Case #" << test << ":\n";
        for (int i = 0; i < r; i++){
            for (int j = 0; j < col; j++){
                cout << arr[i][j];
            }
            cout << "\n";
        }
    }
    return 0;
}
