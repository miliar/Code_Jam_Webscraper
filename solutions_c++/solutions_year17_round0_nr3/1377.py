//
//  main.cpp
//  test
//
//  Created by 수익 조 on 2017. 1. 5..
//  Copyright © 2016년 수익 조. All rights reserved.
//
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
    unsigned long long exp[64]={1,1,};
    int testcase = 0,i;
    //freopen("/Users/Sik/Downloads/C-large.in.txt","r",stdin);
    scanf("%d", &testcase);
    for(i=2;i<64;++i)exp[i]=exp[i-1]<<1;
    for(int t = 1; t <= testcase; t++) {
        unsigned long long N,K,area,index,temp,n1,n2,n2_num;
        scanf("%llu%llu",&N,&K);
        for(i=0;K>=exp[i+1];++i);
        area=i;
        index=K-exp[i]+1;
        temp=N-(exp[i]-1);
        n1=temp/exp[i];
        n2=n1+1;
        n2_num=temp%exp[i];
        if(index<=n2_num)n1=n2;
        printf("Case #%d: %llu %llu\n",t,n1/2,n1%2?n1/2:n1/2-1);
    }
    return 0;
}
