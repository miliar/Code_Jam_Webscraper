#include<cstdio>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<vector>
#include<deque>
using namespace std;

int T;
int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("outputC.txt","w",stdout);
    scanf("%d",&T);
    for(int j=1;j<=T;j++){
        priority_queue<long long> pq;
        long long temp,N,K,a,b;
        scanf("%lld %lld",&N,&K);
        pq.push(N);
        while(K--){
            temp = pq.top();
            if(temp==0){
                a=b=0;
                break;
            }
            pq.pop();
            if(temp%2==0){
                pq.push(((temp/2)-1));
                b=(temp/2)-1;
            }
            else{
                pq.push((temp/2));
                b=temp/2;
            }
            pq.push((temp/2));
            a=temp/2;
        }
        printf("Case #%d: %d %d\n",j,a,b);
    }
    return 0;
}

