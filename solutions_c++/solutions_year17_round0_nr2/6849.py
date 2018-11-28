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
bool isnodescending(long long x){
    long long y = x;
    bool isnotdescending = true;
    int last = y%10;//低位
    while (y / 10 != 0 && isnotdescending) {
        int temp = y%10;//高位
        if (temp <= last) {
            last = temp;
            y = y/10;
        }else{
            isnotdescending = false;
        }
    }
    return isnotdescending && (y <= last);
}

int main(){
    int sumCount;
    vector<long long> resultList;
    char nums[19];
    FILE *fp=fopen("/Users/lixiangqian/Downloads/B-large.in.txt","r");
    FILE *fw=fopen("/Users/lixiangqian/Downloads/B-large.out.txt","w");
    if (fp) {
        fscanf(fp,"%d",&sumCount);
        for (int j=0; j<sumCount; j++) {
            fscanf(fp,"%s\n",nums);
            int i = 0;
            long long y = 0;
                while (nums[i] != '\0' && nums[i+1] != '\0') {
                    if (nums[i] > nums[i+1]) {
                        //从i+1开始之后的
                        int t = i;
                        nums[i] = nums[i] - 1;
                        int j = i+1;
                        while (nums[j] != '\0') {
                            nums[j] = '9';
                            j++;
                        }
                        i = t==0?0:t-1;
                    }else{
                        i ++;
                    }
                }
            int k = 0;
            if (nums[0] == '0') {
                k =1;
            }
            while (nums[k] != '\0') {
                y = y*10 + nums[k] - '0';
                k++;
            }
            resultList.push_back(y);
        }
    }
    for (int i=0; i<sumCount; i++){
        fprintf(fw,"Case #%d: %lld\n", i+1, resultList[i]);
    }
    return 0;
}
