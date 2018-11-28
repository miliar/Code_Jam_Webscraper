#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 105

int tests, n, p, f[104], answer;
int d3[NMAX][NMAX][NMAX], d2[NMAX][NMAX];

int main (){
    int val;
    
    scanf("%d", &tests);
    
    d2[0][0] = 1;
    for(int i = 0; i <= 100; i++)
        for(int j = 0; j <= 100 - i; j++){
            //printf("%d %d %d\n",i,j, d2[i][j]);
            int rest = j % 2;
            d2[i + 1][j] = max(d2[i + 1][j], d2[i][j] + (!rest));
            d2[i][j + 1] = max(d2[i][j + 1], d2[i][j] + rest);
        }
    
    d3[0][0][0] = 1;
    for(int i = 0; i <= 100; i++)
        for(int j = 0; j <= 100 - i; j++)
            for(int k = 0; k <= 100 - i - j; k++) {
                int rest = (j + 2 * k) % 3;
                d3[i + 1][j][k] = max(d3[i + 1][j][k], d3[i][j][k] + (rest == 0));
                d3[i][j + 1][k] = max(d3[i][j + 1][k], d3[i][j][k] + (rest == 2));
                d3[i][j][k + 1] = max(d3[i][j][k + 1], d3[i][j][k] + (rest == 1));
            }
            
    /*d4[0][0][0] = 1;
    for(int i = 0; i <= 100; i++)
        for(int j = 0; j <= 100 - i; j++)
            for(int k = 0; k <= 100 - i - j; k++) {
                int rest = (j + 2 * k) % 3;
                d3[i + 1][j][k] = max(d3[i + 1][j][k], d3[i][j][k] + (rest == 0));
                d3[i][j + 1][k] = max(d3[i][j + 1][k], d3[i][j][k] + (rest == 2));
                d3[i][j][k + 1] = max(d3[i][j][k + 1], d3[i][j][k] + (rest == 1));
            }*/
    
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d",&n,&p);
        for(int i = 1; i <= n; i++) {
            scanf("%d",&val);
            f[val % p]++;
        }
        
        if(p == 3) {
            answer = d3[f[0]][f[1]][f[2]];
            if((f[1] + 2 * f[2]) % p == 0)
                answer--;
        }
        else {
            answer = d2[f[0]][f[1]];
            if((f[1] & 1) == 0)
                answer--;
        }
        printf("Case #%d: %d\n", t, answer);
        memset(f, 0, sizeof(f));
    }
    
    return 0;
}