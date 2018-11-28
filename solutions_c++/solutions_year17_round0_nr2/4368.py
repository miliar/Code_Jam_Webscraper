#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

unsigned long long max_tidy(unsigned long long N) {
	int i,j;
	deque<int> v;
	while(N>0) {
		v.push_front(N%10);
		N = N/10;
	}
	for(i=v.size()-1;i>0;i--) {
		if(v[i] < v[i-1]) {
			for(j=i;j<v.size() && v[j] != 9;j++) {
				v[j] = 9;
			}
			v[i-1]--;
		}
	}
	N = 0;
	for(i=0;i<v.size();i++) {
		N = 10*N + v[i];
	}
	return N;
}

int main() {
	int i=1,T;
	unsigned long long N;
	cin>>T;
	while(i<=T) {
		cin>>N;
		cout<<"Case #"<<i<<": "<<max_tidy(N)<<"\n";
		i++;
	} 
	return 0;
}