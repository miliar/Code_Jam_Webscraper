#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll t,tc=1,r,c;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    while(t--){
        cin >> r >> c;
        char mat[r+2][c+2] = {'A'};
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++){
                cin >> mat[i][j];
            }
        }
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++){
                if(mat[i][j] != '?'){
                    int k=1,l=1;
                    while(mat[i+k][j] == '?'){
                        mat[i+k][j] = mat[i][j];
                        k++;
                    }
                    while(mat[i-l][j] == '?'){
                        mat[i-l][j] = mat[i][j];
                        l++;
                    }
                }
            }
        }
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++){
                if(mat[i][j] == '?'){
                    int f=1,b=1;
                    while(mat[i][j+f] == '?'){
                        f++;
                    }
                    if(j+f <= c)mat[i][j] = mat[i][j+f];
                    else{
                        while(mat[i][j-b] == '?'){
                            b++;
                        }
                        if(j-b >= 1)mat[i][j] = mat[i][j-b];
                    }
                }
            }
        }
        cout << "Case #" << tc << ":\n";
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++)cout << mat[i][j];
            cout << endl;
        }
        tc++;
    }
    return 0;
}
