#include<bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    long long int t,i,test,w,j,n,k,cur,no;
    vector<long long int> neww;
    scanf("%lld",&test);
    for(w=1;w<=test;w++){
        scanf("%lld%lld",&n,&k);
        neww.clear();
        neww.push_back(1);
        neww.push_back(n+2);
        pair<long long int,long long int> lengthh;
        for(j=1;j<=k;j++){
            cur=-1;
            for(i=1;i<neww.size();i++){
                if(neww.at(i)-neww.at(i-1)==1) continue;
                no=(neww.at(i-1)+neww.at(i))/2;;
                pair<long long int,long long int> varr=make_pair(no-neww.at(i-1)-1,neww.at(i)-no-1);
                if(cur==-1){
                    cur=no;
                    lengthh=varr;
                }
                if(neww.at(i-1)%2==neww.at(i)%2){
                    if(min(lengthh.first,lengthh.second) < min(varr.first,varr.second)){
                        cur=no;
                        lengthh=varr;
                    }
                    else if(min(lengthh.first,lengthh.second)==min(varr.first,varr.second)){
                        if(max(lengthh.first,lengthh.second)<max(varr.first,varr.second)){
                            cur=no;
                            lengthh=varr;
                    }}}
                else{
                    if( min(lengthh.first,lengthh.second) < min(varr.first,varr.second)){
                        cur=no;
                        lengthh=varr;
                    }
                    else if(min(lengthh.first,lengthh.second)==min(varr.first,varr.second)){
                        if(max(lengthh.first,lengthh.second)<max(varr.first,varr.second)){
                            cur=no;
                            lengthh=varr;
                    }}
                    no++;
                    varr=make_pair(varr.first+1,varr.second-1);
                    if(min(lengthh.first,lengthh.second)<min(varr.first,varr.second)){
                        cur=no;
                        lengthh=varr;
                    }
                    else if(min(lengthh.first,lengthh.second)==min(varr.first,varr.second)){
                        if(max(lengthh.first,lengthh.second)<max(varr.first,varr.second)){
                            cur=no;
                            lengthh=varr;
                    }}}}
            neww.push_back(cur);
            sort(neww.begin(),neww.end());
        }
        printf("Case #%lld: %lld %lld\n",w,lengthh.second,lengthh.first);
    }
}
