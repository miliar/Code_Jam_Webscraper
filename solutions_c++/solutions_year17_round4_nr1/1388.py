#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

int nTest;
typedef pair<int,int> ii;
int a[222];
int f[111][111][111][4];
int cnt[11];
int n, p;
int dq(int x, int y, int z, int left){
    if (x == 0 && y == 0 && z == 0)
        return 0;
    if (f[x][y][z][left] > -1)
        return f[x][y][z][left];

    int res = 0;
    if (x > 0){
        int need = 1;
        need -= left;
        need %= p;
        if (need < 0) need += p;
        res = max(res, dq(x - 1, y, z, need != 0 ? p - need  : 0 ));
        // printf("1->%d\n", res);
    }
    if (y > 0){
        int need = 2;
        need -= left;
        need %= p;
        if (need < 0) need += p;
        res = max(res, dq(x, y - 1, z, need != 0 ? p - need  : 0  ));
        // printf("2->%d\n", res);
    }
    if (z > 0){
        int need = 3;
        need -= left;
        need %= p;
        if (need < 0) need += p;
        res = max(res, dq(x, y, z - 1, need != 0 ? p - need  : 0  ));
        // printf("3->%d\n", res);
    }
    // printf("<-\n");
    if (left == 0)
        res ++;
    f[x][y][z][left] = res;
    return res;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        scanf("%d %d", &n, &p);
        for (int i = 0; i < n; i++){
            scanf("%d", a + i);
        }
        memset(cnt, 0, sizeof(cnt));
        memset(f, -1, sizeof(f));

        for (int i = 0; i < n; i++){
            cnt[a[i] % p]++; 
        }
        // for (int i = 0; i < p; i++){
        //     printf("%d ", cnt[i]);
        // }
        // printf("\n");
        int res = dq(cnt[1], cnt[2], cnt[3], 0);
        printf("%d\n", res + cnt[0]);
    }
}