#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    FILE *inf, *outf;
    inf=fopen("A-large.in","r");
    outf=fopen("A-large-result.in","w");
    
    int T;
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        int D,N;
        int k,s;
        double maxVal=0.;
        double ret;
        fscanf(inf,"%d %d",&D,&N);
        for(int j=0;j<N;j++){
            fscanf(inf,"%d %d",&k,&s);
            maxVal = max((D * 1.0 - k) / s, maxVal);
        }
        ret = D * 1.0 / maxVal;
        fprintf(outf,"Case #%d: %6f\n",i+1,ret);       
    }
}