#include<cstdio>

using namespace std;
int test,T,n,p,num[4],i,s,a;

int main(){
    scanf("%d",&test);
    for(T=1;T<=test;T++){
        scanf("%d %d",&n,&p);
        for(i=0;i<p;i++)num[i]=0;
        for(i=0;i<n;i++){
            scanf("%d",&a);
            num[a%p]++;
        }
        s=0;
        if(p==2){
            s+=num[0];
            s+=(num[1]+1)/2;
        }
        else if(p==3){
            s+=num[0];
            if(num[1]>num[2]){
                s+=num[2];
                num[1]-=num[2];
                s+=(num[1]+2)/3;
            }
            else{
                s+=num[1];
                num[2]-=num[1];
                s+=(num[2]+2)/3;
            }
        }
        else{
            s+=num[0];
            s+=(num[2])/2;
            num[2]%=2;
            if(num[1]>num[3]){
                s+=num[3];
                num[1]-=num[3];
                s+=(num[1])/4;
            }
            else{
                s+=num[1];
                num[3]-=num[1];
                s+=(num[3])/4;
            }
            if((num[1]+num[3])%4==0&&num[2]>0)s+=2;
            else if(num[2]>0&&(num[1]+num[3])%4==3)s+=2;
            else if((num[1]+num[3])%4>0||num[2]>0)s++;
        }
        printf("Case #%d: %d\n",T,s);
    }
}
