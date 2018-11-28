#include<cstdio>
double max(int a,int b){
    return a>b?a:b;
}
int main(){
    freopen("input.in","r+",stdin);
    freopen("output.out","w+",stdout);
    int t,n;
    double loc,speed,x,maxi;
    scanf("%d",&t);
    for(int T=1;T<=t;T++){
        maxi=0;
        scanf("%lf %d",&x,&n);
        for(int i=0;i<n;i++){
            scanf("%lf %lf",&loc,&speed);
            if((x-loc)/speed>maxi)
                maxi=(x-loc)/speed;
        }
        printf("Case #%d: %.8lf\n",T,x/maxi);
    }
}
