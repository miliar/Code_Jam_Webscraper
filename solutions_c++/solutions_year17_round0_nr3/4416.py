#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){

		long n,k;
		cin>>n>>k;
		priority_queue<long> vsort;
		vsort.push(n);
		long m=1;
		while(m<=k){
			long s = vsort.top();
			vsort.pop();
			vsort.push(s/2);
			vsort.push((s-1)/2);
			if(m==k){
				cout<< "Case #"<<i<<": "<<(s/2)<<" "<<((s-1)/2)<<"\n";
			}
			m++;
		}

	}	

}