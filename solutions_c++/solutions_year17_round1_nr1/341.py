#include <bits/stdc++.h>
using namespace std;

int n,r,c;
char ch;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&n);
    for(int k = 1; k <= n; k++){
        scanf("%d%d\n",&r,&c);
        vector<vector<char>> grid(r);
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                scanf("%c",&ch);
                grid[i].push_back(ch);
            }
            scanf("\n");
        }
        for(auto &i : grid){
            for(int j = 0; j < i.size(); j++){
                if(i[j] == '?') continue;
                for(auto p = j-1; p >= 0; p--){
                    if(i[p] == '?') i[p] = i[j];
                    else break;
                }
                for(auto p = j+1; p < i.size(); p++){
                    if(i[p] == '?') i[p] = i[j];
                    else break;
                }
            }
        }
        for(int i = 0; i < r; i++){
            if(grid[i][0] != '?'){
                for(int j = i-1; j >= 0; j--){
                    if(grid[j][0] == '?') grid[j] = grid[i];
                    else break;
                }
                for(int j = i+1; j < r; j++){
                    if(grid[j][0] == '?') grid[j] = grid[i];
                    else break;
                }
            }
        }
        printf("Case #%d:\n",k);
        for(auto i : grid){
            for(char j : i){
                printf("%c",j);
            }
            printf("\n");
        }
    }
}