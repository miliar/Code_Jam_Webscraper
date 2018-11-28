#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

bool isGood(char* input){
    int goodCnt = 0;
    for(int i=0;i<strlen(input);i++){
        if(input[i]=='+')goodCnt++;
    }
    if(goodCnt == strlen(input))return true;
    return false;
}

int main(){
    FILE *inf, *outf;
    inf=fopen("A-large.in","r");
    outf=fopen("A-large-result.in","w");
    
    int T,N;
    char input[1002];
    int size;
    string s;
    int ret = 0;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        ret=0;
        s.clear();
        fscanf(inf,"%s",input);
        fscanf(inf,"%d",&size);
        for(int i=0;i<strlen(input)-(size-1);i++){
            if(input[i]=='+')continue;
            ret++;
            for(int j=0;j<size;j++){
                if(input[i+j]=='-')input[i+j]='+';
                else input[i+j]='-';
            }
        }    
        if(isGood(input))ret=ret;
        else ret=-1;
        if(ret>=0){
            fprintf(outf,"Case #%d: %d\n",i+1,ret);
        }else{
            fprintf(outf,"Case #%d: %s\n",i+1,"IMPOSSIBLE");
        }
            
    }
//    getchar();
}