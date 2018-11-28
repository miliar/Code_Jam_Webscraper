#include <bits/stdc++.h>
#define LL long long int

using namespace std;

const int INF = 0x7FFFFFFF;

void
Filework(void){
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
}

double a[505];
int n, p;
double ha[505];
double low[505][505];
double high[505][505];
double g[505][505];
int pos[505];

const
int
cmp(double x1, double x2){
    return x1 <= x2;
}

LL
work(){
    int i, j, k;
    LL minn;
    LL maxx;
    LL num;
    double val;
    int flag;
    LL mm;
    LL total = 0;
    mm = INF;
    minn = INF;
    maxx = -1;
    for(i = 1; i <= n; i ++){
        sort(g[i] + 1, g[i] + 1 + p, cmp);
       // for(j = 1; j <= p; j ++)
       //     cout << g[i][j] << ' ';
       // cout << endl;
    }
    for(i = 1; i <= p; i ++){
            for(j = 1; j <= n; j ++){
                low[j][i] = g[j][i] * 10.0/11.0;
                high[j][i] = g[j][i] * 10.0 / 9.0;
            }
    }
    for(i = 1; i <= n; i ++){
        minn = min(minn, (LL)(low[i][1] / ha[i]));
        maxx = max(maxx, (LL)(high[i][p] / ha[i]));
    }
    for(i = minn - 1; i <= maxx + 1; i ++){
        mm = INF;
        for(j = 1; j <= n; j ++)
            pos[j] = p + 1;
        for(j = 1; j <= n; j ++){
            val = i * ha[j];
            num = 0;
            for(k = 1; k <= p; k ++){
                if(val <= high[j][k] && val >= low[j][k]){
                    num ++;
                    pos[j] = min(pos[j], k);
                   // high[j][k] = -INF;
                   // low[j][k] = INF;
                }
            }
            mm = min(mm, num);
          //  cout << i << ' ' << mm << endl;
        }
        for(j = 1; j <= n; j ++){
            for(k = pos[j]; k <= pos[j] + mm - 1; k ++){
                high[j][k] = -INF;
            }
        }
        total += mm;
    }
    return total;
}

int
main(){

	Filework();

	int T, t;
	int i, j;
	LL sum;

    scanf("%d", &T);
    for(t = 1; t <= T; t ++){
        printf("Case #%d: ", t);
        scanf("%d%d", &n, &p);
        for(i = 1; i <= n; i ++){
            scanf("%lf", &ha[i]);
        }
        sum = 0;
        for(i = 1; i <= n; i ++){
            for(j = 1; j <= p; j ++){
                scanf("%lf", &g[i][j]);

            }
        }

        sum = work();
        printf("%lld\n", sum);
    }

return 0;
}
