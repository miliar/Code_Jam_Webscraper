#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(long long index=0;index<T;index++){
		long long N,K;
		cin>>N>>K;
		priority_queue<long long > pq;
		K--;
		pq.push(N);
		while(K--){
			long long x = pq.top();
			pq.pop();
			x--;
			long long a,b;
			if(x&1){
				a=x/2+1;
				b=x/2;
			}
			else{
				a=x/2;
				b=x/2;
			}
			if(a!=0)pq.push(a);
			if(b!=0)pq.push(b);

		}
		cout<<"Case #"<<index+1<<": ";
		long long val=pq.top();
		if(val&1){
			val--;
			cout<<val/2<<" "<<val/2<<endl;
		}
		else{
			val--;
			cout<<val/2+1<<" "<<val/2<<endl;
		}
	}
	return 0;
}
