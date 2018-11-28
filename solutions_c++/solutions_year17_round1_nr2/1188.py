#include <bits/stdc++.h>
using namespace std;

const int maxN = 100, maxP = 100;

const double eps = 0.0001;
int g[maxN];

int a[maxN][maxP];

int n, p;

int work(){
    cin >> n >> p;
    for(int i = 0; i < n; i++)
        cin >> g[i];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < p; j++)
            cin >> a[i][j];


if(n == 1){
    int cnt = 0;
    for(int i = 0; i < p; i++){
            int low = (a[0][i]/1.1)/g[0] - 2;

            int high = (a[0][i]/0.9)/g[0] + 2;

            for(int k = max(low, 1); k <= high; k++){
                if(g[0]*k*0.9 <= a[0][i] && a[0][i] <= g[0]*k*1.1){
                    cnt += 1;
                    break;
                }
            }

    
        }
    return cnt;

}else if(n == 2){

    int permu[maxN];

    for(int i = 0; i < p; i++)
        permu[i] = i;

    int maxCnt = 0;
    do{
        int cnt = 0;
        for(int i = 0; i < p; i++){
            int p0low = (a[0][i]/1.1)/g[0] - 2;

            int p0high = (a[0][i]/0.9)/g[0] + 2;
    
            int p1low = (a[1][permu[i]]/1.1)/g[1] - 2;

            int p1high = (a[1][permu[i]]/0.9)/g[1] + 2;
    
            if(p0low > p1high || p1low > p0high)
                continue;

            int low = max(p0low, p1low);
            int high = min(p0high, p1high);
            for(int k = max(low, 1); k <= high; k++){
                if(g[0]*k*0.9 <= a[0][i] && a[0][i] <= g[0]*k*1.1 && g[1]*k*0.9 <= a[1][permu[i]] && a[1][permu[i]] <= g[1]*k*1.1){
                    cnt += 1;
                    break;
                }
            }
        }

        maxCnt = max(maxCnt, cnt);
    }while(next_permutation(permu, permu+p));

    return maxCnt;

}else{
    return 0;
}
}


int main(){
    int t;
    scanf("%d\n", &t);
    for(int i = 1; i <= t; i++){
        printf("Case #%d: %d\n", i, work());
    }
    return 0; 
}