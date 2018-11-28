#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long 
int main(){

	int t,n,k;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){

		scanf("%d%d",&n,&k);
		priority_queue<int> pq;
		pq.push(n);
		//cout<<"n= "<<n<<"k= "<<k<<'\n';
		k--;
		while(k>0){
			int top=pq.top();
		//	cout<<"inside loop k= "<<k<<" top= "<<top<<'\n';
			
			pq.pop();
			int x= top/2;
			if(top%2){
				pq.push(x);
				pq.push(x);
			}
			else{
				pq.push(x-1);
				pq.push(x);
			}
			k--;
		}

		int top=pq.top();
		
		int ans=top/2;
		//cout<<"top= "<<top<<"ans "<<ans<<'\n';
		if(top%2 || top==0){
			printf("Case #%d: %d %d\n",i,ans,ans);
			}
			else{
				printf("Case #%d: %d %d\n",i,ans,ans-1);
			}
	}
	return 0;
}