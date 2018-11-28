//
//  main.cpp
//  a
//
//  Created by   kimtaehoon on 2017. 4. 30..
//  Copyright © 2017년   kimtaehoon. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
bool tmr(pair<double,double> a,pair<double,double> b)
{
    if(a.first>b.first) return true;
    if(a.first<b.first) return false;
    return false;
}
int main(int argc, const char * argv[]) {
    FILE *in=fopen("/Users/kimtaehoon/Desktop/code jam round c/a/a/in.txt", "r");
    FILE *out=fopen("/Users/kimtaehoon/Desktop/code jam round c/a/a/out.txt", "w");
    int t;
    fscanf(in,"%d",&t);
    for(int q=1;q<=t;q++)
    {
        double n,k;
        fscanf(in,"%lf %lf",&n,&k);
        vector<pair<double,double> > arr(1111);
        vector<pair<double,double> > arr2(1111);
        for(int e=0;e<n;e++)
        {
            double a,b;
            fscanf(in,"%lf %lf",&a,&b);
            arr[e]={a,b};
        }
        for(int e=0;e<n;e++)
        {
            arr2[e].first=2*M_PI*arr[e].first*arr[e].second;
            arr2[e].second=arr[e].first;
        }
        sort(arr2.begin(),arr2.begin()+n,tmr);
        double maxs=0;
        for(int e=0;e<n;e++)
        {
            double pp=1,tms=arr2[e].second*arr2[e].second*M_PI+arr2[e].first;
            for(int p=0;p<n;p++)
            {
                if(e==p) continue;
                if(pp==k)
                {
                    maxs=max(maxs,tms);
                    break;
                }
                if(arr2[p].second<=arr2[e].second)
                {
                    pp++;
                    tms+=arr2[p].first;
                }
            }
            if(pp==k)
            {
                maxs=max(maxs,tms);
            }
        }
        
        fprintf(out,"Case #%d: %.9lf\n",q,maxs);
    }
    return 0;
}
