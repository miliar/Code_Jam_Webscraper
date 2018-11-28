#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("Asmall.txt", "r", stdin);
    freopen("Asmallout.txt", "w", stdout);
    int t, tc, r, c, mark[100], cnt, i, j, k, l;
    char s[100][100], temp[100];
    cin >> tc;
    for(t = 1; t <= tc; t++){
        for(i = 0; i < 40; i++) mark[i] = 1;
        cin >> r >> c;
        for(i = 1; i <= r; i++){
            for(j = 1; j <= c; j++){
                cin >> s[i][j];
                if(s[i][j] != '?'){
                    mark[s[i][j] - 65] = 1;
                }
            }
        }
        for(i = 1; i <= r; i++){
            for(j = 1, cnt = 0; j <= c; j++){
                if(s[i][j] != '?' && cnt == 0){
                    cnt++;
                    for(k = 1; k < j; k++){
                        s[i][k] = s[i][j];
                    }
                    for(k = j + 1; ; k++){
                        if(s[i][k] != '?') break;
                        s[i][k] = s[i][j];
                    }
                }
                else if(s[i][j] != '?' && cnt != 0){
                    cnt++;
                    for(k = j + 1; k <= c; k++){
                        if(s[i][k] != '?') break;
                        s[i][k] = s[i][j];
                    }
                }
            }
            if(cnt == 0){
                mark[i] = 0;
            }
        }
        for(i = 1, cnt = 0; i <= r; i++){
            if(mark[i] == 1 && cnt == 0){
                cnt++;
                for(j = 1; j <= c; j++){
                    temp[j] = s[i][j];
                }
                for(k = 1; k < i; k++){
                    for(l = 1; l <= c; l++){
                        s[k][l] = temp[l];
                    }
                }
                for(k = i + 1; k <= r; k++){
                    if(mark[k] == 1) break;
                    for(l = 1; l <= c; l++){
                        s[k][l] = temp[l];
                    }
                }
            }
            if(mark[i] == 1 && cnt != 0){
                for(j = 1; j <= c; j++){
                    temp[j] = s[i][j];
                }
                for(k = i + 1; k <= r; k++){
                    if(mark[k] == 1) break;
                    for(l = 1; l <= c; l++){
                        s[k][l] = temp[l];
                    }
                }
            }
        }

        cout << "Case #" << t << ":" << endl;
        for(i = 1; i <= r; i++){
            for(j = 1; j <= c; j++){
                cout << s[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
