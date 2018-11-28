#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){

    int t,i,j,p,k;
    int el,x,y,n;
    priority_queue< int >pq;
    scanf("%d",&t);
    for(p=1 ; p<=t ; p++){

		scanf("%d %d",&n,&k);
		pq.push(n);

		while(k--){
			el = pq.top();
			pq.pop();
            el--;
            x = el/2;
            y = el - x;
			pq.push(x);
			pq.push(y);
		}
		printf("Case #%d: %d %d\n",p,y,x);

		while(!pq.empty())
			pq.pop();
    }
	return 0;
}
