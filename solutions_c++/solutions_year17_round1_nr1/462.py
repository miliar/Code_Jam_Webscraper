//
//  main.cpp
//  leetcode3
//
//  Created by 赵毅 on 4/8/17.
//  Copyright © 2017 赵毅. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

char mx[30][30];

int main(void){
    int T;
    FILE *fin=stdin;
    fscanf(fin,"%d",&T);
    for(int I=1;I<=T;I++){
        int n,m;
        fscanf(fin, "%d %d", &n,&m);
        for(int i=0;i<n;i++){
            fscanf(fin,"%s", mx[i]);
        }
        for(int i=0;i<n;i++){
            char ch='?';
            for(int j=0;j<m;j++){
                if(mx[i][j]!='?') ch=mx[i][j];
                if(mx[i][j]=='?' && ch!='?'){
                    mx[i][j]=ch;
                }
            }
        }
        for(int i=0;i<n;i++){
            char ch='?';
            for(int j=m-1;j>=0;j--){
                if(mx[i][j]!='?') ch=mx[i][j];
                if(mx[i][j]=='?' && ch!='?'){
                    mx[i][j]=ch;
                }
            }
        }
        for(int i=1;i<n;i++){
            char ch=0;
            for(int j=0;j<m;j++){
                if(mx[i][j]!='?') ch=1;
            }
            if(ch==0){
                for(int j=0;j<m;j++){
                    mx[i][j]=mx[i-1][j];
                }
            }
        }
        for(int i=n-1-1;i>=0;i--){
            char ch=0;
            for(int j=0;j<m;j++){
                if(mx[i][j]!='?') ch=1;
            }
            if(ch==0){
                for(int j=0;j<m;j++){
                    mx[i][j]=mx[i+1][j];
                }
            }
        }
        printf("Case #%d: \n", I);
        for(int i=0;i<n;i++){
            printf("%s\n", mx[i]);
        }
    }
}
