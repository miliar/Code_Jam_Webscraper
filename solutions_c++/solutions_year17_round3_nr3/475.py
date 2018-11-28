#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 1005
#define eps 0.0000001

int n, k, tests;
double u;
pair<double, int> p[NMAX];

void solveSmall() {
    p[++n] = make_pair(1, 1);
    while(1) {
        sort(p + 1, p + n + 1);
      //  printf("Aveam %lf %d si %lf %d si %lf\n", p[1].x, p[1].y, p[2].x, p[2].y, u);
        if((p[2].x - p[1].x) * p[1].y + eps < u) {
            u -= (p[2].x - p[1].x) * p[1].y;
            p[2].y += p[1].y;
            p[1].x = 1;
        }
        else {
            p[1].x += u / p[1].y;
            break;
        }
    }
    double answer = 1;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= p[i].y; j++)
            answer *= p[i].x;
        //printf("%lf %d %lf\n", p[i].x, p[i].y, answer);
    }
    printf("%.9lf\n", answer);
}

int main (){

    scanf("%d",&tests);
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        for(int i = 1; i <= n; i++) {
            scanf("%lf", &p[i].x);
            p[i].y = 1;
        }
        printf("Case #%d: ", t);
        if(k == n) {
            solveSmall();
            memset(p,0,sizeof(p));
            continue;
        }
    }
    
    return 0;
}

