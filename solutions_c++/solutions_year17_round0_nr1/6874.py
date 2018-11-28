//
//  googleoj1.cpp
//  leecode
//
//  Created by lixiangqian on 17/4/8.
//  Copyright © 2017年 lixiangqian. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <math.h>
#include <stdlib.h>
using namespace std;
int main(){
    int sumCount,k=0;
    char x[1001];
    vector<int> resultList;
    FILE *fp=fopen("/Users/lixiangqian/Downloads/A-large.in.txt","r");
    FILE *fw=fopen("/Users/lixiangqian/Downloads/A-large.out.txt","w");
    if (fp) {
        fscanf(fp,"%d",&sumCount);
        for (int j=0; j<sumCount; j++) {
            fscanf(fp,"%s %d\n",x,&k);
            int i = 0;
            int count = 0;
            bool find = true;
            while (x[i] != '\0' && find) {
                if (x[i] == '-') {
                    count ++;
                    for (int j = 0; j < k; j++) {
                        if (x[i+j] != '\0') {
                            x[i+j] = x[i+j]=='+'?'-':'+';
                        }else{
                            find = false;
                            break;
                        }
                    }
                    i++;
                }else{
                    i++;
                }
            }
            if (!find) {
                resultList.push_back(-1);
            }else{
                resultList.push_back(count);
            }
        }
    }
    for (int i=0; i<sumCount; i++){
        if (resultList[i] == -1) {
            fprintf(fw,"Case #%d: IMPOSSIBLE\n", i+1);
        }else{
            fprintf(fw,"Case #%d: %d\n", i+1, resultList[i]);
        }
    }
    return 0;
}
