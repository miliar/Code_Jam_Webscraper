#include<stdio.h>
#include<algorithm>
using namespace std;

int n,m,T;
double Dis[1011];
double Speed[1011];
double in[111][111];
double a[1011];
double nowD[1011];
double nowSp[1011];
double nowT[1011];
int now;

double nextD[1011];
double nextSp[1011];
double nextT[1011];
int next;

int main() {
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1-out.txt","w",stdout);
    int i,j,k;
    int g,gg;
    double p,q,r;
    double t,tt,ttt;
scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++) {
        scanf("%lf %lf",&Dis[i],&Speed[i]);
    }
    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
            scanf("%lf",&in[i][j]);
            if(i + 1 == j) {
                a[i] = in[i][j];
            }
        }
    }

    for(i=0;i<m;i++) {
        scanf("%d %d",&g,&gg);
    }
    now = 0;
    nowT[0] = 0.0;
    next = 0;
    for(i=0;i<n-1;i++) {
        now = 0;
        p = -1.0;
        for(j=0;j<next;j++) {
            nowD[j] = nextD[j];
            nowSp[j] = nextSp[j];
            nowT[j] = nextT[j];
            if(p == -1.0) p = nextT[j];
            else  {
                if(p > nextT[j]) p = nextT[j];
            }
            now ++;
        }
        nowD[now] = Dis[i];
        nowSp[now] = Speed[i];
        if(p == -1.0) nowT[now] = 0.0;
        else nowT[now] = p;
        now ++;
        next = 0;
        for(j=0;j<now;j++) {
            if(nowD[j] >= a[i]) {
                nextD[next] = nowD[j] - a[i];
                nextSp[next] = nowSp[j];
                nextT[next] = nowT[j] + (a[i] / nowSp[j]);
                next++;
            }
        }

       // for(j=0;j<next;j++) printf("%lf %lf %lf\n",nextD[j],nextSp[j],nextT[j]);printf(">>>>> %lf\n",a[i]);
    }

    p = -1.0;
    for(i=0;i<next;i++) {
        if(p == -1.0) p = nextT[i];
        else {
            if(p > nextT[i]) p = nextT[i];
        }
    }

    printf("Case #%d: %lf\n",ii+1,p);
}


    return 0;
}
