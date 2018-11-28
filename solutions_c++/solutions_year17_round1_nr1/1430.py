#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for(int f=1; f<=n; f++){
        int r, c;
        cin >> r >> c;
        vector<string> v(r);
        for(int i=0; i<r; i++)
            cin >> v[i];


        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(v[i][j] != '?'){
                    int k;
                    for(k=0; k < j; k++){
                        v[i][k] = v[i][j];
                    }

                    k++;
                    for(; k < c; k++){
                        if(v[i][k] == '?')
                            v[i][k] = v[i][k - 1];
                    }
                    break;
                }
            }
        }

        if(v[0][0] == '?'){
            for(int j=1; j<r; j++){
                if(v[j][0] != '?'){
                    v[0] = v[j];
                    break;
                }
            }
        }
        for(int i=1; i<r; i++){
            if(v[i][0] == '?')
                v[i] = v[i-1];
        }
        cout << "Case #" << f << ":" << endl;
        for(int i=0; i<r; i++)
            cout << v[i] << endl;
    }
    return 0;
}
