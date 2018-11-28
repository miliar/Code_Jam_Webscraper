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
		string N;
		cin>>N;
		bool again;
		do
		{
			again=false;
			for(size_t i{1};i<N.size();++i)
				if(N[i-1]>N[i])
				{
					--N[i-1];
					for(size_t j{i};j!=N.size();++j)
						N[j]='9';
					again=true;
					break;
				}
		}while(again);
		if(N.front()=='0')
			N.erase(0,1);
		cout<<"Case #"<<(case_i+1)<<": "<<N<<'\n';
	}
}