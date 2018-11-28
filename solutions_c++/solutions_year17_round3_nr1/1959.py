//
//  google1a1.cpp
//  leecode
//
//  Created by lixiangqian on 17/4/28.
//  Copyright © 2017年 lixiangqian. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <math.h>
#include <stdlib.h>
using namespace std;
int main(){
        int sumCount;
        vector<long double> resultList;
        FILE *fp=fopen("/Users/lixiangqian/Downloads/A-large.in-2.txt","r");
        FILE *fw=fopen("/Users/lixiangqian/Downloads/A-large.out.txt","w");
        if (fp) {
            fscanf(fp,"%d",&sumCount);
            for (int i =0; i < sumCount; i++) {
                int n, k;
                fscanf(fp, "%d %d", &n,&k);
                int largestindex = 0;
                long largestradius = 0;
                unsigned long long heigthcount = 0;
                unsigned long long largestmm = 0;
                unsigned long long largesttotalmm = 0;
                long double result;
                long nums[n][2];
                for (int j =0; j < n; j++) {
                    fscanf(fp, "%ld %ld", &nums[j][0], &nums[j][1]);
                    
                }
                vector<long double> tempresults(n);
                for (int jj = 0; jj < n ; jj++) {
                    long long templargestmm = pow(nums[jj][0],2)+2*nums[jj][0]*nums[jj][1];
                   
                    heigthcount = 0;
                    largestmm = templargestmm;
                    largestindex = jj;
                    largestradius = nums[jj][0] ;
                    largesttotalmm = templargestmm;
                    
                    multiset<unsigned long long , less<unsigned long long> > resultheight;
                    //unsigned long long t = nums[largestindex][1] * nums[largestindex][0] * 2;
                    //resultheight.insert(t);
                    for (int j = 0; j < n; j++) {
                        if (j != largestindex && nums[j][0] <= largestradius) {
                            unsigned long long s = nums[j][1] * nums[j][0] * 2;
                            
                            if (k>1) {
                                if (resultheight.size() < k-1) {
                                    
                                    resultheight.insert(s);
                                }else{
                                    multiset<unsigned long long, less<unsigned long long> >::iterator least_list = resultheight.begin();
                                    
                                    if(s > *(resultheight.begin())){
                                        resultheight.erase(least_list);
                                        resultheight.insert(s);
                                    }
                                }
                            }
                        }
                    }
                    for (multiset<unsigned long long, less<unsigned long long> >::iterator r = resultheight.begin(); r != resultheight.end(); r++) {
                        heigthcount += *r;
                        //cout<<*r<<endl;
                    }
                    result = (largestmm + heigthcount)*M_PI;
                    tempresults[jj] = result;
                }
                
                sort(tempresults.begin(), tempresults.end());
                resultList.push_back(tempresults[n-1]);
            }
        }
        for (int i=0; i<sumCount; i++){
            fprintf(fw,"Case #%d: %.9Lf\n", i+1, resultList[i]);
        }
        return 0;
}
