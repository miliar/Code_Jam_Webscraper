#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	freopen("p1C_17_output.txt","w",stdout);
	// freopen("p1C_17_outputLarge.txt","w",stdout);

	int t;
	long long int n,k,x,y;

	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%lld%lld",&n,&k);
		priority_queue<long long int> p;
		p.push(n);
		while(k>1){
		    n=p.top();
		    p.pop();
			if(n%2==0){
				n/=2;
				p.push(n);
				p.push(n-1);
			}else{
				n=(n-1)/2;
				p.push(n);
				p.push(n);
			}
			k--;
		}
		x = p.top();
		if(x%2){
			x=(x-1)/2;
			y=x;
		}else{
			x/=2;
			y=x-1;
		}
		printf("Case #%d: %lld %lld\n",i,x,y);
	}
	return 0;
}