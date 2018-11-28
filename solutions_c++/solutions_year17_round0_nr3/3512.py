#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;
long long int K, N, a1, a2;
int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	printf("Case #%d: ",cases);
    	scanf("%lld %lld",&N,&K);
    	priority_queue<long long int> q;
    	q.push(N);
    	for(int i=1; i<=K; i++){
    		long long int cur = q.top(); q.pop();
    		if(cur == 0) a1=a2=0;
    		else{
    			cur--;
    			a2 = cur/2; a1 = cur-a2;
			}

    		q.push(a1); q.push(a2);
		}
		printf("%d %d\n",a1, a2);
	}
    return 0;
}
