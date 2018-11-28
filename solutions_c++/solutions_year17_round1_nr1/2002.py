#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

void solve(vector<string> &A){
    int C = A[0].size();
    int R = A.size();
    vector<vector<bool>> B(R, vector<bool>(C, false));
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
            if(A[i][j] != '?')
                B[i][j] = true;

    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            if(A[i][j] != '?' && B[i][j]){
                char ch = A[i][j];
                int l, r;
                for(l=j-1; l>=0; l--){
                    if(A[i][l] != '?') break;
                } l++;
                for(r=j+1; r<C; r++){
                    if(A[i][r] != '?') break;
                } r--;
                for(int k=l; k<=r; k++) A[i][k] = ch;
                int pos = i+1;
                bool flag = true;
                while(pos < R && flag){
                    for(int k=l; k<=r; k++)
                        if(A[pos][k] != '?') flag = false;
                    if(flag)
                        for(int k=l; k<=r; k++) A[pos][k] = ch;
                    pos++;
                }
                pos = i-1;
                flag = true;
                while(pos >= 0 && flag){
                    for(int k=l; k<=r; k++)
                        if(A[pos][k] != '?') flag = false;
                    if(flag)
                        for(int k=l; k<=r; k++) A[pos][k] = ch;
                    pos--;
                }
            }
        }
    }
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int R, C;
        cin >> R >> C;
        vector<string> A(R);
        for(int j=0; j<R; j++)
            cin >> A[j];
        cout << "Case #" << i+1 << ": " << endl;
        solve(A);
        for(int j=0; j<R; j++){
            for(int k=0; k<C; k++){
                cout << A[j][k];
            }
            cout << endl;
        }
    }

    return 0;
}
