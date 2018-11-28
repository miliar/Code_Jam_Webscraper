#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;

int main (){
    int T;
    scanf("%d" ,&T);
    for (int t=1;t<=T;t++){
    //for each test
    int max,h;
    scanf("%d %d", &max, &h);
    double slowest = 0.000000000;
    for(int i=0;i<h;i++){
        double a,b;
        scanf("%lf %lf", &a, &b);
        double dis = max-a;
        double dt = dis/b;
        if(dt>slowest)slowest=dt;
    }
    double odp = max/slowest;
    printf("Case #%d: %.6lf\n", t, odp );
        
    }
    return 0;
}