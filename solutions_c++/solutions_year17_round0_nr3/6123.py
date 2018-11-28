#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;

class ullcmp{
	public:
		bool operator() (ull lhs, ull rhs){
			return lhs>=rhs;
		}
};


int main(){
	uint T;ull N,K,maxLR,minLR;
	cin>>T;
	for(uint t=0;t<T;t++){
		cin>>N>>K;

		set<ull,ullcmp> numset;
		numset.insert(N);
		for(ull j=0;j<K;j++){
			ull term=*(numset.begin());
			numset.erase(numset.begin());
			minLR=term-(term/2)-1;
			maxLR=term/2;
			numset.insert(minLR);
			numset.insert(maxLR);
		}

		cout<<"Case #"<<(t+1)<<": "<<maxLR<<" "<<minLR<<endl;

	}
}
