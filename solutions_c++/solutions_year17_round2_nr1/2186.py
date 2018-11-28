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
#define INF 1000000002

pair<int, int> v[NMAX];
double answer;
int t, d, n;

int main (){
    
    scanf("%d",&t);
    for(int test = 1; test <= t; test++) {
        scanf("%d%d",&d,&n);
        for(int i = 1; i <= n; i++) {
            int a, b;
            scanf("%d%d",&a,&b);
            v[i] = make_pair(a,b);
        }
        sort(v + 1, v + n + 1);
        
        double answer = INF;
        for(int i = n; i >= 1; i--) {
            double timp = (double)v[i].y / ((double)d - v[i].x);
            answer = min(answer, timp);
        }
        
        answer *= d;
        printf("Case #%d: %.6lf\n", test, answer);
    }
    
    return 0;
}