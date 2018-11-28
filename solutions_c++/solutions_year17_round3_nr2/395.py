#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <cstring>
#include <vector>
using namespace std;

int nTest;
typedef pair<int,int> ii;
int job[2222];
int f[2222][1111][3][3];
int dp(int pos, int remA, int isA, int aFirst){
    if (f[pos][remA][isA][aFirst] > -1)
        return f[pos][remA][isA][aFirst];

    if (remA == 0 && pos == 1440){
        return isA != aFirst ? 1 : 0;
    }
    if (remA < 0)
        return 1000000;
    if (pos >= 1440)
        return 1000000;
    // if (1440 - pos < remA)
    //     return 1000000;



    int ans = 1000000;
    if (job[pos] == 0 || job[pos] == 2){
        //A turn
        int cost = 0;
        if (!isA)
            cost++;

        ans =  min(ans, dp(pos + 1, remA - 1, 1, aFirst) + cost);
    }
    if (job[pos] == 0 || job[pos] == 1){
        //B turn
        int cost = 0;
        if (isA)
            cost++;

        ans =  min(ans, dp(pos + 1, remA, 0, aFirst) + cost);
    }
    f[pos][remA][isA][aFirst] = ans;
    return ans;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        int n, m;
        scanf("%d %d", &n, &m);
        memset(f, -1, sizeof(f));
        for (int i = 0; i <= 2000; i++)
            job[i] = 0;
        for (int i = 0; i < n; i++){
            int s, f;
            scanf("%d %d", &s, &f);
            for (int j = s; j < f; j++)
                job[j] = 1;
        }
        for (int i = 0; i < m; i++){
            int s, f;
            scanf("%d %d", &s, &f);
            for (int j = s; j < f; j++)
                job[j] = 2;
        }

        int res = dp(0, 720, 1, 1);
        res = min(res, dp(0, 720, 0, 0));
        printf("%d\n", res);
    }
}