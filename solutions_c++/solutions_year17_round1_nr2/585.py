#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

int n, p;
int r[100];
int q[100][100];
int poi[100];

int getmin (int eve, int need) {
    int num = (double)eve / ((double)need * 1.1) - 1;
    //cout << num << endl;
    while ( !((double)(num) * need * 0.9 <= (double)eve && (double)num * need * 1.1 >= (double)eve)) {
        
        if ((double)(num) * need * 0.9 > (double)eve) {
            return -1;
        }
        num++;
    }
    return num;
}



int getmax (int eve, int need) {
    int num = (double)eve / ((double)need * 0.9) + 10;
    while ( !((double)(num) * need * 0.9 <= (double)eve && (double)num * need * 1.1 >= (double)eve)) {
        
        if ((double)num * need * 1.1 < (double)eve) {
            return -1;
        }
        num--;
    }
    return num;
}

void getnext (int num) {
    while (getmin(q[num][poi[num]], r[num]) == -1 && poi[num] <= p) {
        poi[num]++;
    }
}

int main(int argc, const char * argv[]) {
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T;
    
    getint(T);
    REP(ca, 1, T) {
        getint(n);
        getint(p);
        int ans = 0;
        REP(i, 1, n) {
            getint(r[i]);
        }
        REP(i, 1, n) {
            REP(j, 1, p) {
                getint(q[i][j]);
            }
            sort(q[i] + 1, q[i] + 1 + p);
        }
        
        REP(i, 1, n) {
            poi[i] = 1;
        }
        
        
        int id = 0, minnum = -1;
        while (1) {
            bool flag = false;
            bool getans = true;
            
            if (id == 0) {
                getnext(1);
                if (poi[1] > p) {
                    flag = true;
                    break;
                }
                id = 1;
                minnum = getmin(q[1][poi[1]], r[1]);
            }
            
            for (int i = 1; i <= n; i++) {
                if (i == id) {
                    continue;
                }
                getnext(i);
                if (poi[i] > p) {
                    flag = true;
                    break;
                }
                while (getmax(q[i][poi[i]], r[i]) < minnum) {
                    poi[i]++;
                    getnext(i);
                    if (poi[i] > p) {
                        flag = true;
                        break;
                    }
                }
                if (poi[i] <= p && getmin(q[i][poi[i]], r[i]) > minnum) {
                    minnum = getmin(q[i][poi[i]], r[i]);
                    id = i;
                    getans = false;
                    break;
                }
            }
            
            if (flag) {
                break;
            }
            
            if (getans) {
                ans++;
                //cout << poi[1] << endl;
                REP(i, 1, n) {
                    poi[i]++;
                }
                id = 0;
            }
            
        }
        printf("Case #%d: %d\n", ca, ans);
        
        
        
    }
    
    return 0;
}









