#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		cout<<"Case #"<<t+1<<": ";
		string S;
		int K;
		cin>>S;
		cin>>K;
		int ans=0;
		bool possible=true;
		for (int i = 0; i < S.size(); ++i)
		{
			if(S[i] == '-')
			{
				// flip
				if(i+K>S.size())continue;
				for (int k = 0; k < K; ++k)
				{
					S[i+k] = S[i+k] == '-'?'+':'-';
				}
				++ans;
			}
		}
		for (int i = 0; i < S.size(); ++i)
		{
			if(S[i] == '-')
			{
				possible = false;
				break;
			}
		}

		if (possible)
		{
			cout<<ans<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}

	}

	return 0;
}