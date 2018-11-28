#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#define LEFT 1
#define RIGHT 0
using namespace std;
const long long maxn=1000000000000000000+5;
long long n,k;
int t;
long long two[100];
int idx=0;
void init(){
    two[0]=1;
    for(idx=1;idx<65;idx++){
        two[idx]=two[idx-1]*2;
//printf("%d %lld\n",idx,two[idx]);
        if(two[idx]>maxn)
            break;

    }
}
long long dfs(int layer,int cnt,int leftOrRight){
    if(layer==0)
        return n;
    int facnt=(cnt+1)/2;
    long long fares=dfs(layer-1,facnt,facnt%2);
    long long res;
    if(leftOrRight==LEFT){
        res=fares/2;
    }
    else{
        res=(fares-1)/2;
    }
    return res;
}
int main()
{
    init();
    FILE*f1=fopen("C-small-2-attempt0.in","r");
    FILE*f2=fopen("C-small-2-attempt0.out","w");
    fscanf(f1,"%d",&t);
    //scanf("%d",&t);
//printf("idx %d\n",idx);
    for(int tt=1;tt<=t;tt++){
        fscanf(f1,"%lld %lld",&n,&k);
        //scanf("%lld %lld",&n,&k);
        long long sum=0;
        int layer;

        for(int i=0;i<=idx;i++){
//printf("sum %lld\n",sum);
            if(sum<k && sum+two[i]>=k){
                layer=i;
//printf("%d\n",layer);
                break;
            }
            sum+=two[i];
        }
        int layerWithOne=0;
        long long tmp=n;
        int cnt=k-sum;
        long long layerFirst[100]; //the first/larger num of each layer
        layerFirst[0]=n;
        while(tmp){
            if(tmp==1)
                break;
            tmp=tmp/2;
            layerFirst[++layerWithOne]=tmp;
        }
//printf("layer1:%d\n",layerWithOne);
        fprintf(f2,"Case #%d: ",tt);
        //printf("Case #%d: ",tt);
//printf("layer:%d layer1:%d cnt:%d\n",layer,layerWithOne,cnt);
        if(layer>=layerWithOne){
            fprintf(f2,"0 0\n");
            //printf("0 0\n");
        }
        else{
            if(layer==0){
                fprintf(f2,"%lld %lld\n",n/2,(n-1)/2);
                //printf("%lld %lld\n",n/2,(n-1)/2);
            }
            else{
                int largerCnt=1,smallerCnt=1;
                if(n/2==(n-1)/2){
                    largerCnt=2;
                    smallerCnt=0;
                }
                else{
                    largerCnt=smallerCnt=1;
                }
                int lastlargerCnt=largerCnt,lastsmallerCnt=smallerCnt;
                for(int i=2;i<=layer;i++){
                    if(layerFirst[i-1]%2==0){
                        largerCnt=lastlargerCnt;
                        smallerCnt=lastsmallerCnt*2+lastlargerCnt;
                    }
                    else{
                        largerCnt=lastlargerCnt*2+smallerCnt;
                        smallerCnt=smallerCnt;
                    }
                    lastlargerCnt=largerCnt;
                    lastsmallerCnt=smallerCnt;
                }
                long long value;
                if(cnt<=largerCnt){
                    value=layerFirst[layer];
                }
                else{
                    value=layerFirst[layer]-1;
                }
//printf("n:%lld k:%d value:%lld\n",n,k,value);
                fprintf(f2,"%lld %lld\n",value/2,(value-1)/2);
                //printf("%lld %lld\n",value/2,(value-1)/2);
            }
            //long long value=dfs(layer,cnt,cnt%2);

        }

    }
    fclose(f1);
    fclose(f2);
    return 0;
}
