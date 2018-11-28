#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<cstdlib>
using namespace std;

int T,N,D;
int k[1005],s[1005];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%d",&T);
    for(int z=1;z<=T;z++){
        memset(k,0,sizeof(k));
        memset(s,0,sizeof(s));
        double ans=-1.0;
        scanf("%d %d",&D,&N);
        for(int i=0;i<N;i++){
            scanf("%d %d",&k[i],&s[i]);
        }
        for(int i=N-1;i>=0;i--){
            double temp=0;
            double temp_d=0;
            temp = (double)D-k[i];
            temp_d = (double)(temp/s[i]);
            ans = max(ans,temp_d);
        }
        double comp = D/ans;
        printf("Case #%d: %.6f\n",z,comp);
    }
    return 0;
}
