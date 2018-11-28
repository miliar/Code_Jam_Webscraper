#include <cstdio>
#include <vector>
using namespace std;

char board[33][33];

int main(){
    int T; scanf("%d", &T);
    for(int ti=1;ti<=T;ti++){
        int n, m; scanf("%d%d", &n, &m);
        for(int i=0;i<n;i++) for(int j=0;j<m;j++)
            scanf(" %c", &board[i][j]);
        vector<int> is_empty_line(33, 0);
        for(int i=0;i<n;i++){
            is_empty_line[i] = true;
            for(int j=0;j<m;j++){
                if(board[i][j] != '?'){
                    is_empty_line[i] = false;
                    break;
                }
            }
            if(is_empty_line[i]) continue;
            for(int j=0;j<m;j++){
                if(board[i][j] != '?'){
                    for(int k=j-1;k>=0;k--){
                        if(board[i][k] == '?') board[i][k] = board[i][j];
                        else break;
                    }
                    for(int k=j+1;k<m;k++){
                        if(board[i][k] == '?') board[i][k] = board[i][j];
                        else break;
                    }
                }
            }
        }
        for(int i=0;i<n;i++){
            if(!is_empty_line[i]){
                for(int j=i-1;j>=0;j--){
                    if(is_empty_line[j]){
                        for(int k=0;k<m;k++){
                            board[j][k] = board[i][k];
                        }
                    }
                    else break;
                }
                for(int j=i+1;j<=n;j++){
                    if(is_empty_line[j]){
                        for(int k=0;k<m;k++){
                            board[j][k] = board[i][k];
                        }
                    }
                    else break;
                }
            }
        }
        printf("Case #%d:\n", ti);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++) printf("%c", board[i][j]);
            printf("\n");
        }
    }
    return 0;
}
