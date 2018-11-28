#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long test,i,j,k,m,neww,ind,n,no;
    scanf("%lld",&test);
    for(j=1;j<=test;j++){
        scanf("%lld",&no);
        for(i=num;i>=1;i--){
            arr=i;
            ind=0;neww=100;
            while(k!=0){
                kk=arr%10;
                if(kk<=neww){
                    neww=kk;
                }
                else{
                    ind=1;
                    break;
                }
                k=k/10;
            }
            if(ind==0){
                no=i;
                break;
            }
        }
        printf("Case #%d: %d\n",j,no);
    }
    return 0;
}
