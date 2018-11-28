#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    FILE *inf, *outf;
    inf=fopen("C-large.in","r");
    outf=fopen("C-large-result.in","w");
    vector<int> modList, modList2;
    int T,N;
    long input, target;
    long nowTarget;
    long ret = 0;
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        long retMax,retMin,retMinCount,retMaxCount;
        fscanf(inf,"%ld %ld",&input, &target);
        nowTarget = target;
        long squareVal=1;
        long nowVal=2;
        long leftVal;
        long finalTarget;
        while((nowVal*2)-1<target){
            squareVal++;
            nowVal*=2;
        }
        leftVal = target - (nowVal-1);

        retMin = (input-1-((input-1)%2))/2;
        retMax = retMin + ((input-1)%2);
        retMinCount=1;
        retMaxCount=1;
        if(target>1){
            for(int j=1;j<squareVal;j++){
                long nowRetMin = retMin;
                long nowRetMax = retMax;
                long nowRetMinCount = retMinCount;
                long nowRetMaxCount = retMaxCount;

                if(nowRetMin % 2 == 0){
                    retMin = (nowRetMin-2)/2;
                    retMax = (nowRetMax)/2;
                    if(nowRetMax % 2 == 1){
                        retMinCount = nowRetMinCount;
                        retMaxCount = nowRetMaxCount * 2 + nowRetMinCount;
                    }else{
                        retMinCount = nowRetMinCount * 2;
                        retMaxCount = nowRetMaxCount * 2;
                    }
                }else{
                    if(nowRetMax % 2 == 1){
                        retMin = (nowRetMin-1)/2;
                        retMax = (nowRetMax-1)/2;
                        retMinCount = nowRetMinCount * 2;
                        retMaxCount = nowRetMaxCount * 2;
                    }else{
                        retMin = (nowRetMin-1)/2;
                        retMax = (nowRetMax)/2;
                        retMinCount = nowRetMinCount * 2 + nowRetMaxCount;
                        retMaxCount = nowRetMaxCount;
                    }
                }
            }
            if(leftVal>retMaxCount){
                finalTarget = retMin;
            }else{
                finalTarget = retMax;
            }
            if(finalTarget%2==1){
                retMin = (finalTarget-1)/2;
                retMax = (finalTarget-1)/2;
            }else{
                retMin = (finalTarget-2)/2;
                retMax = finalTarget/2;
            }
        }
        printf("Case #%d: %ld %ld\n",i+1,retMax,retMin); 
        fprintf(outf,"Case #%d: %ld %ld\n",i+1,retMax,retMin);       
    }
}