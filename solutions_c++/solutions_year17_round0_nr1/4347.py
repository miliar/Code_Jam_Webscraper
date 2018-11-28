#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		bool impos = false;
		string S;
		cin>>S;
		int K;
		cin>>K;
		bool stop = false;
		int j = 0;
		int count = 0;
		while(!impos && !stop)
		{
			for(; j<S.size();j++)
			{
				if(S[j]=='-')
				{
					if(j+K > S.size())
					{
						impos = true;
						break;
					}
					else
					{
						for(int k=j;k<j+K;k++)
						{
							if(S[k]=='-')
								S[k] = '+';
							else
								S[k] = '-';
						}
						count++;
						break;

					}
				}
			}
			if(j==S.size())
				stop = true;
		}
		if(impos)
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i<<": "<<count<<endl;

	}
}