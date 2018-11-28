#include <iostream>

int T;
long long N,K;

int main(){
	std::cin>>T;
	for(int i=0;i<T;i++){
		std::cin>>N>>K;
		long long biggest=1;
		
		while(biggest*2<=K)//first split into 'biggest power of 2<K' parts
			biggest*=2;
		
		long long q,r,last;//we have parts of size q and q+1, with r of the latter 
		q=(N-biggest+1)/biggest;
		r=(N-biggest+1)%biggest;
		last=(K-biggest+1>r)?q:q+1;
		
		std::cout<<"Case #"<<i+1<<": "<<last/2<<' '<<(last-1)/2<<'\n';
		
	}
	return 0;
}