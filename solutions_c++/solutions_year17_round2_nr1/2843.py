#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>


using namespace std;

typedef long long int lli;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,d,n,k,s;
    scanf("%d",&t);
    double time, may;
    for(int c=1; c<=t; c++){
        scanf("%d %d",&d,&n);
        may = 0.0;
        for(int i=0; i<n; i++){
            scanf("%d %d",&k,&s);
            time = ((double)(d-k))/((double)s);
            if(time>may){
                may = time;
            }
        }
        printf("Case #%d: %.6f\n",c,((double)d)/may);
    }

    return 0;
}
