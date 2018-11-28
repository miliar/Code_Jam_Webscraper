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
#include <math.h>
using namespace std;

int mx[60][60];
int req[60];
int indexs[60];

int inv[60][2];

bool TEST=false;

int main(void){
    int T;
//    FILE *fin=stdin;
    FILE *fin=fopen("/Users/enyaning/Downloads/B-large.in-4.txt","r");
    fscanf(fin,"%d",&T);
    for(int I=1;I<=T;I++){
        int n,m;
        int res=0;
        fscanf(fin, "%d %d", &n,&m);
        
        for(int i=0;i<n;i++){
            fscanf(fin, "%d", req+i);
            indexs[i]=0;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                fscanf(fin, "%d", mx[i]+j);
            }
            sort(mx[i], mx[i]+m);
        }
        while(true){
            for(int i=0;i<n;i++){
                inv[i][0]=ceil(mx[i][indexs[i]]/1.1/req[i]);
                inv[i][1]=floor(mx[i][indexs[i]]/0.9/req[i]);
                if(TEST) cout<<inv[i][0]<<" "<<inv[i][1]<<endl;
            }
            int min=inv[0][0];
            int max=inv[0][1];
            for(int i=1;i<n;i++){
                if(min<inv[i][0]) min=inv[i][0];
                if(max>inv[i][1]) max=inv[i][1];
            }
            if(min>0 && min<=max){
                res+=1;
                if(TEST) cout<<min<<" "<<max<<": ";
                for(int i=0;i<n;i++){
                    if(TEST) cout<<indexs[i]<<" ";
                    indexs[i]+=1;
                }if(TEST) cout<<endl;
            }else{
                double min_frac=1e100;
                int min_index=-1;
                for(int i=0;i<n;i++){
                    int frac=double(mx[i][indexs[i]])/req[i];
                    if(min_frac>frac){
                        min_frac=frac;
                        min_index=i;
                    }
                }
                indexs[min_index]+=1;
            }
            int i;
            for(i=0;i<n;i++){
                if(indexs[i]>=m) break;
            }
            if(i!=n) break;
        }
        
        printf("Case #%d: %d\n", I, res);
    }
}
