#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

map<long long, long long> amounts;
vector<long long> lengths;
long long index;

bool compare(long long a, long long b){
	return a > b;
}

long long getCount(){
	long long cLength = lengths[index];
	long long cAmount = amounts[lengths[index]];

	long long nLength = (cLength - 1)/2;

	//cout<<"\t\t"<<cLength<<' '<<cAmount<<endl;
	if((cLength % 2) == 0){ //two lengths created
		if(!amounts[nLength+1]) lengths.push_back(nLength+1);
		amounts[nLength+1] += cAmount;

		if(!amounts[nLength]) lengths.push_back(nLength);
		amounts[nLength] += cAmount;
	} else { //one length created
		if(!amounts[nLength]) lengths.push_back(nLength);
		amounts[nLength] += 2 * cAmount;
	}

	sort(lengths.begin(), lengths.end(), compare);
	return cAmount;
}

int main(){
	int t;
	cin>>t;


	for(int i=0;i<t;i++){
		long long n,k;
		long long count = 0;

		cin>>n>>k;

		lengths.push_back(n);
		amounts[n] = 1;

		while(count < k){
			count += getCount();
			//cout<<count<<endl;
			index++;
		}
		index--;

		//printf("n: %lld, k: %lld, index: %lld, length: %lld, count: %lld\n", n, k, index, lengths[index], count);

		long long nLength = (lengths[index] - 1)/2;

		printf("Case #%d: ", i+1);
		if(lengths[index] % 2 == 0){ //two solutions
			printf("%lld %lld\n", nLength + 1, nLength);
		} else { //same solution
			printf("%lld %lld\n", nLength, nLength);
		}

		//clear data
		amounts.clear();
		lengths.clear();
		index = 0;
	}
	return 0;
}