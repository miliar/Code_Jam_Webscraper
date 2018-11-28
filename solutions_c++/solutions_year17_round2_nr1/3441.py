#include <bits/stdc++.h>
#define LL long long int

using namespace std;

const int INF = 0x7FFFFFFF;

void
Filework(void){
	freopen("t1.in", "r", stdin);
	freopen("t1.out", "w", stdout);
}

struct
NODE{
    double position;
    double speed;
}horse[1005];

int n;

const
int
cmp(NODE p, NODE q){
    return p.position < q.position;
}

int
main(){

	Filework();

    int T, t;
    int i, j;
    double dis;
    double minspeed, mintime, mindis;
    double ans;

    scanf("%d", &T);
    for(t = 1; t <= T; t ++){
        printf("Case #%d: ", t);
        scanf("%lf%d", &dis, &n);
        for(i = 1; i <= n; i ++){
            scanf("%lf%lf", &horse[i].position, &horse[i].speed);
        }
        sort(horse + 1, horse + 1 + n, cmp);
        minspeed = horse[1].speed;
        mintime = (dis - horse[1].position) / horse[1].speed;
        mindis = horse[1].position;
        for(i = 2; i <= n; i ++){
        /*
            if(horse[i].speed >= minspeed){
                break;
            }
            mintime += (horse[i].position - mindis) / (minspeed - horse[i].speed);
            if(horse[i].position + mintime * horse[i].speed >= dis){
                break;
            }
            mindis = horse[i].position + mintime * horse[i].speed;
            minspeed = horse[i].speed;
        */
            if((dis - horse[i].position) / horse[i].speed > mintime){
                mintime = (dis - horse[i].position) / horse[i].speed;
            }
        }
   //     ans = horse[1].position / ((dis - horse[1].position) / horse[1].speed) + horse[1].speed;
   //     if(mintime == 0){
   //         printf("%.6lf\n", ans);
    //    }
//       else
            printf("%.6lf\n", dis / mintime);
    }


return 0;
}
