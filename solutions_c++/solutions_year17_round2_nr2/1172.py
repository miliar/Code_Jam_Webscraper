// Google Code Jam 2017 Round 1B - B
// https://code.google.com/codejam/contest/8294486/dashboard#s=p1
// 2017.04.22

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define ll long long
#define N 111111
#define md 1000000007
using namespace std;

int t;
ll n, r, o, y, g, b, v;
char u[] = "ROYGBV", nd[][3] = {"GR", "VY", "BO", "YB", "RB", "RY"};

int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        scanf("%lld%lld%lld%lld%lld%lld%lld", &n, &r, &o, &y, &g, &b, &v);
        ll x = y + b + r - v - o - g;
        ll vv[] = {2 * g, 2 * v, 2 * o, x - 2 * (r - g), x - 2 * (y - v), x - 2 * (b - o)};

        bool fail = false;
        char st = 0;
        for(int i = 0; i < 6; i++)
            if(vv[i] < 0)
                fail = true;
            else if(vv[i] > 0)
                st = nd[i][0];
        if(fail){
            printf("Case #%d: IMPOSSIBLE\n", s);
            continue;
        }
        printf("Case #%d: ", s);
        while(n--){
            printf("%c", st);
            for(int i = 0; i < 6; i++)
                if(vv[i] && (nd[i][0] == st || nd[i][1] == st)){
                    vv[i]--;
                    if(nd[i][0] == st) st = nd[i][1]; else st = nd[i][0];
                    break;
                }
        }
        printf("\n");
    }
}
