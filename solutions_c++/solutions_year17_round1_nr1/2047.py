#include <cstdio>

using namespace std;

char str[28][28];

int main(){

    int t;
    scanf("%d", &t);

    int tc = 0;

    while(t--){
        int r, c;
        scanf("%d %d", &r, &c);
        for(int i=0; i<r; i++)scanf("%s", str[i]);
        bool used['Z'+3] = {};
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(str[i][j] != '?'){
                    if(used[str[i][j]])continue;
                    used[str[i][j]] = true;
                    int y[2] = {j,j};
                    while(y[0]-1 >= 0 && str[i][y[0]-1] == '?'){
                        y[0]--;
                    }
                    while(y[1]+1 < c && str[i][y[1]+1] == '?'){
                        y[1]++;
                    }
                    for(int b=y[0]; b<=y[1]; b++){
                        str[i][b] = str[i][j];
                    }
                    int x = i;
                    while(x-1 >= 0){
                        bool flag = true;
                        for(int b=y[0]; b<=y[1]; b++){
                            flag &= (str[x-1][b] == '?');
                        }
                        if(flag){
                            for(int b=y[0]; b<=y[1]; b++)str[x-1][b] = str[i][j];
                        }else
                            break;
                        x--;
                    }
                    x = i;
                    while(x+1 < r){
                        bool flag = true;
                        for(int b=y[0]; b<=y[1]; b++){
                            flag &= (str[x+1][b] == '?');
                        }
                        if(flag){
                            for(int b=y[0]; b<=y[1]; b++)str[x+1][b] = str[i][j];
                        }else{
                            break;
                        }
                        x++;
                    }
                }
            }
        }
        printf("Case #%d:\n", ++tc);
        for(int i=0; i<r; i++)printf("%s\n", str[i]);
    }

}
