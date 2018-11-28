//
//  main.cpp
//  test
//
//  Created by 수익 조 on 2017. 1. 5..
//  Copyright © 2016년 수익 조. All rights reserved.
//
#include <stdio.h>

int main(){
    int t,T;
    scanf("%d",&T);
    for(t=78;t<=T;++t){
        int i,j,k,len;
        char N[22];
        scanf("%s",&N);
        for(i=0;N[i];++i);
        len=i;
        for(i=0;i<len;++i){
            for(j=0;j<len-1;++j){
                if(N[j]>N[j+1]){
                    --N[j];
                    for(k=j+1;k<len;++k) N[k]='9';
                    break;
                }
            }
            if(j==len-1) break;
        }
        printf("Case #%d: %s\n",t,N[0]!='0'?N:N+1);
    }
    return 0;
}
