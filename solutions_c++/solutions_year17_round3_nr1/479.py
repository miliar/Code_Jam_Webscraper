#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define radius first
#define height second
#define NMAX 1005
#define eps 0.0000001
#define pi 3.141592653589793238

pair<int,int> pancake[NMAX];
int tests, n, k;

long long getCost(pair<int,int> pancake) {
    return (long long)pancake.radius * pancake.height;
}

inline int cmp(const pair<int,int>& a, const pair<int,int>& b) {
    return getCost(a) > getCost(b);
}

int main (){
    
    scanf("%d", &tests);
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d",&n,&k);
        for(int i = 1; i <= n; i++)
            scanf("%d%d",&pancake[i].radius, &pancake[i].height);
        sort(pancake + 1, pancake + n + 1);
        double answer = 0;
        for(int i = k; i <= n; i++) {
            double cost = pi * pancake[i].radius * pancake[i].radius + (double)pancake[i].height * ((double)2 * pi * pancake[i].radius);
            //printf("%d %.9lf\n", i, cost);
            sort(pancake + 1, pancake + i, cmp);
            for(int j = 1; j < k; j++)
                cost += (double)pancake[j].height * ((double)2 * pi * pancake[j].radius);
            answer = max(answer, cost);
        }
        printf("Case #%d: %.9lf\n", t, answer);
        memset(pancake, 0, sizeof(pancake));
    }
    
    return 0;
}

