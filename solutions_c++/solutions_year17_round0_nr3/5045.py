#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;

int main() {
	int tc,n,k,mid,l,r,aux;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        priority_queue<int> bath;
        scanf("%d %d\n",&n,&k);
        bath.push(n);
        for(int j=0;j<k;j++){
            aux=bath.top();bath.pop();
            //printf("%d\n",aux);
            mid=aux/2;
            bath.push(mid);bath.push(aux-mid-1);
            if(j==(k-1)){
                l=mid;
                r=aux-mid-1;
            }
        }
        printf("Case #%d: %d %d\n",i,max(l,r),min(l,r));
    }
	return 0;
}