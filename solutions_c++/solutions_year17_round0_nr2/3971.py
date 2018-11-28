#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

bool isGood(long input){
    bool check=true;
    vector<int> coList;
    long val = 10;
    while(input > 0){
        long nowTarget = input%val;
        coList.push_back(nowTarget/(val/10));
        input-=nowTarget;
        val*=10;
    }
    for(int i=0;i<coList.size()-1;i++){
        if(coList[i]<coList[i+1])check=false;
    }
    return check;
}

int main(){
    FILE *inf, *outf;
    inf=fopen("B-small-attempt0.in","r");
    outf=fopen("B-small-attempt0-result.in","w");
    
    int T,N;
    long input;
    long ret = 0;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        ret=0;
        long nowTarget = 0;
        long val = 10;
        fscanf(inf,"%ld",&input);
        while(!isGood(input)){
            cout<<input<<endl;
            nowTarget = input%val;
            val*=10;
            input-=(nowTarget+1);
        }
        ret = input;  
        fprintf(outf,"Case #%d: %ld\n",i+1,ret);       
    }
}