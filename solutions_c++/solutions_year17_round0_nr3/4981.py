#include<bits/stdc++.h>

using namespace std;

priority_queue <long long> prior;

int main()
{
	int T;
	cin>>T;
	long long N,K;
	long long first,second,third,fourth;
	for(int count_test=1;count_test<=T;++count_test)
    {
		cin>>N>>K;
		long long var=N;
		for(int i=0;i<K;i++){
			--var;
			first=var/2;
			second=var-first;
			prior.push(first);
			prior.push(second);
			third=min(first,second);
			fourth=max(first,second);
			var=prior.top();
			prior.pop();
		}
		cout<<"Case #"<<count_test<<": "<<fourth<<" "<<third<<endl;
		while(!prior.empty()){
			prior.pop();
		}
	}
return 0;
}
