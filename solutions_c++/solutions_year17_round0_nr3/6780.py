#include <cstdio>
#include <algorithm>
#include <vector>

std::pair <int, int> tam;

int main(){
    int t, n, k, left, right, ctemp, cont, mark, anterior, maior;
    bool fa, fb;
    int flag;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        scanf("%d%d", &n, &k);
        tam.first = tam.second = 0;
        int stalls[n + 2];
        stalls[0] = stalls[n + 1] = 0;
        for(int j = 1; j <= n; j++)
            stalls[j] = 1;
        if(n % 2 == 0){
            stalls[n / 2] = 0;
            flag = 1;
        }
        else{
            stalls[(n / 2) + 1] = 0;
            flag = 2;
        }
        for(int a = 1; a < k; a++){
            flag = 0;
            cont = 0;
            tam.first = 0;
            for(int j = 1; j < n + 2; j++){
                if(stalls[j] == 1){
                    cont++;
                }
                else{
                    cont++;
                    if(cont > tam.first){
                        tam.first = cont;
                        tam.second = j - cont;
                    }
                    cont = 0;
                }
            }
            stalls[(tam.first / 2) + tam.second] = 0;
        }
        int a, b, ca = 0, cb = 0;
        if(flag == 1){
            a = n / 2;
            b = a;
        }
        else if(flag == 2){
            a = (n / 2) + 1;
            b = a;
        }
        else{
            a = (tam.first / 2) + tam.second;
            b = (tam.first / 2) + tam.second;
        }
        fa = fb = false;
        while(true){
            if(!fa){
                a--;
                ca++;
            }
            if(!fb){
                b++;
                cb++;
            }
            if(stalls[a] == 0)
                fa = true;
            if(stalls[b] == 0)
                fb = true;
            if(fa && fb)
                break;
        }
        ca--;
        cb--;
        printf("Case #%d: %d %d\n", i, std::max(ca, cb), std::min(ca, cb));
        //for(int j = 0; j < n + 2; j++)
            //printf("%d ", stalls[j]);
        //printf("\n");
    }
    return 0;
}
