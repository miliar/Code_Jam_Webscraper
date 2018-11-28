#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 2005
#define TMAX 1440
#define INF 1000000000

int tests, n, m;
pair<int,int> papa[NMAX], mama[NMAX];
int d[NMAX][NMAX][2];

int main (){

    scanf("%d",&tests);
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d",&n,&m);
        for(int i = 1; i <= n; i++) {
            scanf("%d%d",&papa[i].x,&papa[i].y);
        }
        sort(papa + 1, papa + n + 1);
        
        for(int i = 1; i <= m; i++) {
            scanf("%d%d",&mama[i].x,&mama[i].y);
        }
        sort(mama + 1, mama + m + 1);
        
        for(int i = 0; i <= TMAX; i++)
            for(int j = 0; j <= TMAX; j++)
                for(int k = 0; k <= 1; k++)
                    d[i][j][k] = INF;
        d[0][0][0] = 0;
        
        int indexP = 1, indexM = 1;
        for(int i = 0; i < TMAX; i++) {
            while(indexP < n && papa[indexP + 1].x <= i)
                indexP++;
            while(indexM < m && mama[indexM + 1].x <= i)
                indexM++;
            for(int j = 0; j <= i; j++) {
                if(i < papa[indexP].x || i >= papa[indexP].y) {
                    d[i + 1][j + 1][0] = min(d[i + 1][j + 1][0], d[i][j][0]);
                    d[i + 1][j + 1][0] = min(d[i + 1][j + 1][0], d[i][j][1] + 1);
                }
                if(i < mama[indexM].x || i >= mama[indexM].y) {
                    d[i + 1][j][1] = min(d[i + 1][j][1], d[i][j][0] + 1);
                    d[i + 1][j][1] = min(d[i + 1][j][1], d[i][j][1]);
                }
            }
        }
        int answer = min(d[TMAX][TMAX / 2][0], d[TMAX][TMAX / 2][1] + 1);
        /////
        
        for(int i = 0; i <= TMAX; i++)
            for(int j = 0; j <= TMAX; j++)
                for(int k = 0; k <= 1; k++)
                    d[i][j][k] = INF;
        d[0][0][1] = 0;
        
        indexP = 1, indexM = 1;
        for(int i = 0; i < TMAX; i++) {
            while(indexP < n && papa[indexP + 1].x <= i)
                indexP++;
            while(indexM < m && mama[indexM + 1].x <= i)
                indexM++;
            for(int j = 0; j <= i; j++) {
                if(i < papa[indexP].x || i >= papa[indexP].y) {
                    d[i + 1][j + 1][0] = min(d[i + 1][j + 1][0], d[i][j][0]);
                    d[i + 1][j + 1][0] = min(d[i + 1][j + 1][0], d[i][j][1] + 1);
                }
                if(i < mama[indexM].x || i >= mama[indexM].y) {
                    d[i + 1][j][1] = min(d[i + 1][j][1], d[i][j][0] + 1);
                    d[i + 1][j][1] = min(d[i + 1][j][1], d[i][j][1]);
                }
            }
        }
        int answer2 = min(d[TMAX][TMAX / 2][0] + 1, d[TMAX][TMAX / 2][1]);
        
        printf("Case #%d: %d\n", t, min(answer, answer2));
        
        memset(papa, 0, sizeof(papa));
        memset(mama, 0, sizeof(mama));
    }
    
    return 0;
}


