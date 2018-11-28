#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
class caballo{
public:
    double pos,vel;
}arr[1005];
bool operator <(caballo c1, caballo c2){
    return c1.pos < c2.pos;
}
int n,cas,a,b;
double d=1000000000,v,t;

int main()
{
    freopen("entrada.in","r",stdin);
    freopen("salida.out","w",stdout);
    scanf("%d",&cas);
    for (int caso=1;caso<=cas;caso++){
        scanf("%lf%d",&d,&n);
        t = 0;
        for (int i=0;i<n;i++){
            scanf("%lf%lf",&arr[i].pos,&arr[i].vel);
        }
        sort(arr,arr+n);
        for (int i=0;i<n;i++){
            t = max(t,(d-arr[i].pos)/arr[i].vel);
        }
        v = d/t;
        printf("Case #%d: %.6lf\n",caso,v);
    }
    return 0;
}
