#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

vector<long> bathroom(long N, long k)
{
	vector<long> result{0,0};
	unordered_map<long,long> space;
	priority_queue<long> sequence; // max heap
	sequence.push(N);
	space[N] = 1;
	long i = 1;
	while(i<=k)
	{
		long n = sequence.top();
		long repeat = space[n];
		n--;
		long first = n/2, second = n-n/2;
		if(k-i+1<=repeat) // return result
			return vector<long>{max(first,second),min(first,second)};
		if(first!=0)
		{
			if(space.count(first)==0)
				sequence.push(first);
			space[first] += repeat;
		}
		if(second!=0)
		{
			if(space.count(second)==0)
				sequence.push(second);
			space[second] += repeat;
		}
		// remove spaces
		space.erase(n+1);
		sequence.pop();
		i += repeat;
	}
	return result;
}

int main()
{
	int t;
	long N, k;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>N>>k;
		vector<long> result = bathroom(N, k);
		cout<<"Case #"+to_string(i+1) + ": " + to_string(result[0]) + ' ' + to_string(result[1])<<endl;
	}
	return 0;
}

