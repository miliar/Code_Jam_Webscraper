#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <math.h>
using namespace std;
double s[1005][2];
int main()
{
    freopen("E://project/code-jam/2017/round1b/A-small-attempt0.in","r",stdin);
    freopen("E://project/code-jam/2017/round1b/a-small.txt","w",stdout);
    int t,k=0,n;
    cin>>t;
    double d;
    while(t--){
        double ans,time;
        scanf("%lf%d",&d,&n);
        for(int i=0;i<n;i++){
            scanf("%lf%lf",&s[i][0],&s[i][1]);
        }
        time=0;
        for(int i=0;i<n;i++){
            if(s[i][0]<d){
                time=max(time,(d-s[i][0])/s[i][1]);
            }
        }
        ans=d/time;
        printf("Case #%d: %.6f\n",++k,ans);
    }
    return 0;
}
