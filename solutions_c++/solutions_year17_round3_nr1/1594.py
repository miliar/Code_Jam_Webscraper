#include<cstdio>
#include<cstdlib>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
# define PI   3.14159265358979323846 
using namespace std;
struct pancake{
    double r;
    double h;
    double bottom(){
        return r*r*PI;
    }
    double side(){
        return 2*PI*r*h;
    }
};
bool compare(pancake a,pancake b){
    return a.r*a.h<b.r*b.h;
}
int main(){
    freopen("inputA","r",stdin);
    freopen("outputA.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int n,k;
        scanf("%d%d",&n,&k);
        pancake p[n];
        for(int i=0;i<n;i++){
            float r,h;
            scanf("%f%f",&r,&h);
            p[i].r=(double)r;
            p[i].h=(double)h;
        }
        sort(p,p+n,compare);
        double ans=0;
        if(k>0){
            for(int i=0;i<n;i++){
                double cans=p[i].bottom()+p[i].side();
                int chosen=1;
                if(k>chosen)
                for(int j=n-1;j>=0;j--){
                    if(j==i||p[j].r>p[i].r)continue;
                    cans+=p[j].side();
                    chosen++;
                    if(chosen==k)break;
                }
                if(chosen<k)continue;
                ans=max(ans,cans);
            }
        }
        float fans=(float)ans;
        printf("Case #%d: %f\n",t,fans);
    }
}
