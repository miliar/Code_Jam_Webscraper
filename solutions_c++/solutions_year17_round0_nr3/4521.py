#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int i=1,T;
	unsigned long long N,K,l,r,cur;
	cin>>T;
	while(i<=T) {
		cin>>N>>K;
		vector<unsigned long long> v{N};
		make_heap(v.begin(),v.end());
		while(K>0) {
			r = v.front()/2;
			l = v.front() -1 -r;
			pop_heap(v.begin(),v.end());
			v.pop_back();
			v.push_back(l);
			push_heap(v.begin(),v.end());
			v.push_back(r);
			push_heap(v.begin(),v.end());
			K--;
		}
		cout<<"Case #"<<i<<": "<<r<<" "<<l<<"\n";
		i++;
	} 
	return 0;
}