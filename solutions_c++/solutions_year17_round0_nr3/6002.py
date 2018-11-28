#include<algorithm>
#include<cassert>
#include<deque>
#include<fstream>
#include<iostream>
#include<numeric>
#include<regex>
#include<stack>
#include<string>
#include<unordered_set>
#include<vector>
using namespace std;

int main()
{
	unsigned T;
	cin>>T;
	for(decltype(T) case_i{0};case_i!=T;++case_i)
	{
		unsigned long long N,K;
		cin>>N>>K;
		vector<decltype(N)> vec(1,N);
		for(decltype(K) i{1};i<=N;++i)
		{
			pop_heap(begin(vec),end(vec));
			const decltype(N) max{vec.back()/2};
			const decltype(N) min{max-(!(vec.back()%2))};
			vec.pop_back();
			if(i==K)
			{
				cout<<"Case #"<<(case_i+1)<<": "<<max<<' '<<min<<'\n';
				break;
			}
			vec.emplace_back(max);
			push_heap(begin(vec),end(vec));
			vec.emplace_back(min);
			push_heap(begin(vec),end(vec));
		}
	}
}