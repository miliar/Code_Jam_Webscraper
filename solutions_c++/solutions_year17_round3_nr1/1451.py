#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;
int N,K;
long dp[1001][1001];
vector<pair<long,long> > sizeList;

long solve(int nowPos, int remain){
    if(remain<=0)return 0;
    if(nowPos==N)return 0;
    long &ret = dp[nowPos][remain];
    if(ret > -1)return ret;

    long h = sizeList[nowPos].second;
    long r = sizeList[nowPos].first;
    long dummy=0;
    if(remain == K){
        dummy = r*r;
    }
    ret = max(solve(nowPos+1,remain), dummy + 2*r*h + solve(nowPos+1, remain - 1));
    return ret;
}

int main(){
    FILE *inf, *outf;
    inf=fopen("A-large.in","r");
    outf=fopen("A-large-result.in","w");
    
    int T;
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        memset(dp,-1,sizeof(dp));
        sizeList.clear();
        fscanf(inf,"%d %d",&N,&K);
        for(int j=0;j<N;j++){
            long r,h;
            fscanf(inf,"%ld %ld",&r,&h);
            sizeList.push_back(make_pair(r,h));
        }
        sort(sizeList.begin(),sizeList.end());
        reverse(sizeList.begin(),sizeList.end());

        long ret = solve(0,K);
        double dret = ret * 3.14159265359;
        fprintf(outf,"Case #%d: %9f\n",i+1,dret);       
    }
}

