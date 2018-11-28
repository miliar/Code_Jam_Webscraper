#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include<queue>
using namespace std;
typedef long long ll;
#define N 1005
#define fr(i,x,y) for(int i=x;i<=y;i++)
#define ms(x,y) memset(x,y,sizeof(x))
int n,k,d,o;


struct ho{
    int d,s;
    bool operator<(const ho&oth)const{
    return d>oth.d;
    }
}a[N];

void doit(){
    scanf("%d%d",&d,&n);
    fr(i,1,n)scanf("%d%d",&a[i].d,&a[i].s);
    sort(a+1,a+1+n);
//    fr(i,1,n)
//        printf("%d %d\n",a[i].d,a[i].s);


    int id=1;
    double tt=double(d-a[id].d)/a[id].s,t1;
    fr(i,2,n){
        int yy=0;
        if (a[i].s<=a[id].s)yy=1;else t1=double(a[id].d-a[i].d)/(a[i].s-a[id].s);
        if (yy||t1>tt) {id=i;tt=double(d-a[id].d)/a[id].s;

        }
    }
    printf("%lf\n",d/tt);


}
int main() {
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--) {
        printf("Case #%d: ",++i);
        doit();
    }
    return 0;
}