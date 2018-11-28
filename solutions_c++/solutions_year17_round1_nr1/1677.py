#include <iostream>

std::string S;
int T;
int R, C;
char arr[27][27];

char findVal(int x,int y){
    for (int i = y-1; 1 <= i; i--){
        if (arr[x][i] != '?'){
            return arr[x][i];
        }
    }
    for (int i = y+1; i <= C; i++){
        if (arr[x][i] != '?'){
            return arr[x][i];
        }
    }
    return '?';
}

char findVal2(int x,int y){
    for (int i = x-1; 1 <= i; i--){
        if (arr[i][y] != '?'){
            return arr[i][y];
        }
    }
    for (int i = x+1; i <= R; i++){
        if (arr[i][y] != '?'){
            return arr[i][y];
        }
    }
    return '?';
}

int main(){
    std::cin >> T;
    for (int t = 1; t <= T; t++){
        std::cin >> R >> C;
        for (int i = 1; i<= R; i++){
            std::cin >> (arr[i]+1);
        }
        for (int i = 1; i <= R; i++){
            for (int j = 1; j <= C; j++){
                if (arr[i][j] == '?'){
                    arr[i][j] = findVal(i, j);
                }
            }
        }
        std::cout << "Case #" << t << ":" << std::endl;
        for (int i = 1; i <= R; i++){
            for (int j = 1; j <= C; j++){
                if (arr[i][j] == '?'){
                    arr[i][j] = findVal2(i, j);
                }
                std::cout << arr[i][j];
            }
            std::cout << std::endl;
        }
    }
    return 0;
}
