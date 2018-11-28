/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   tidymnum.cpp
 * Author: davidtompul
 *
 * Created on April 9, 2017, 12:51 AM
 */

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
using namespace std;


int main() {
    char input[20];
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%s",input);
        int ln = strlen(input);
        for(int j=0;j<ln;j++){
            if(((j+1)<ln) && input[j]>input[j+1]){
                int a = j;
                int valA = input[a];
                input[a]-=1;
                while(a-1>=0 && valA==input[a-1]){
                    input[a-1]-=1;
                    input[a]='9';
                    a--;
                }
                while(j+1<ln){
                    input[j+1]='9';
                    j++;    
                }
            }
        }
        printf("Case #%d: ",i);
        int x=0;
        while(input[x]<='0')x++;
        for(;x<ln;x++)printf("%c",input[x]);
        printf("\n");
    }
    return 0;
}

