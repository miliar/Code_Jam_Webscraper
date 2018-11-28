
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <queue>
using namespace std;

int main(){

    int T,j=1,N,K,Ls,Rs;
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);

    cin>>T;
    
    while(j<=T){
    	priority_queue<int> pq;
    	cin>>N>>K;
    	pq.push(N);

    	//iterate till K
    	for(int i=1;i<=K;i++){
    		int top = pq.top();
    		pq.pop();
    		if(top%2==0){
    			Ls=top/2-1;
    			Rs=top/2;
    		}
    		else{
    			Ls=top/2;
    			Rs=Ls;
    		}
    		pq.push(Ls);
    		pq.push(Rs);
    	}
        cout<<"Case #"<<j<<": "<<max(Ls,Rs)<<" "<<min(Ls,Rs)<<endl;
        j++;
    }
    return 0;
}
