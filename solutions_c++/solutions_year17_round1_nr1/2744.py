#include<iostream>
#include<vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        int r, c;
        cin >> r >> c;
        vector<vector<char> > cake(r, vector<char>(c));
        vector<int> check(30);
        int dir[4][2] = {0, -1, 0, 1, -1, 0, 1, 0};
        for(int j = 0; j < r; j++){
            for(int k = 0; k < c; k++)cin >> cake[j][k];
        }
        
        for(int j = 0; j < r; j++){
            for(int k = 0; k < c; k++){
                char ch = cake[j][k];
                if(ch == '?')continue;
                if(check[ch - '0'])continue;
                int cnt1 = 0;
                int cnt2 = 0;
                for(int l = 0; l < 4; l++){
                    int nrow = j + dir[l][0];
                    int ncol = k + dir[l][1];
                    if((nrow < r && nrow >= 0) && (ncol < c && ncol >= 0) && cake[nrow][ncol] == '?'){
                        while((nrow < r && nrow >= 0) && (ncol < c && ncol >= 0) && cake[nrow][ncol] == '?'){
                            cake[nrow][ncol] = ch;
                            nrow += dir[l][0];
                            ncol += dir[l][1];
                            if(l == 0)cnt1++;
                            else if(l == 1)cnt2++;
                        }
                    }
                    if(l == 1 && (cnt1 || cnt2)){
                        int row = j - 1;
                        int cnt = 0;
                        while(row >= 0){
                            for(int m = k - cnt1; m < k + cnt2 + 1; m++){
                                if(cake[row][m] != '?'){
                                    cnt++;
                                    break;
                                }
                            }
                            if(cnt)break;
                            for(int m = k - cnt1; m < k + cnt2 + 1; m++)cake[row][m] = ch;
                            row--;
                        }
                        row = j + 1;
                        cnt = 0;
                        while(row < r){
                            for(int m = k - cnt1; m < k + cnt2 + 1; m++){
                                if(cake[row][m] != '?'){
                                    cnt++;
                                    break;
                                }
                            }
                            if(cnt)break;
                            for(int m = k - cnt1; m < k + cnt2 + 1; m++)cake[row][m] = ch;
                            row++;
                        }
                        break;
                    }
                }
                check[ch - '0'] = 1;
            }
        }
        cout << "Case #" << i << ":" << '\n';
        for(int j = 0; j < r; j++){
            for(int k = 0; k < c; k++)cout << cake[j][k];
            cout << '\n';
        }
    }

    return 0;
}
