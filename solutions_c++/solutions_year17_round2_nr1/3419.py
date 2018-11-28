#include <bits/stdc++.h>
using namespace std;
 
int main(){
    long long s,k,d;
    int t,n;
    double ans,maxi=0;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
    	maxi=0;
        scanf("%ld %d",&d,&n);
        for(int j=0;j<n;j++){
            scanf("%ld %ld",&k,&s);
            maxi=max(maxi,double(d-k)/s);
            //printf("maxi=%f\n",maxi);
        }
        printf("Case #%d: %.6f\n",i,d/maxi);
    }
    return 0;
}