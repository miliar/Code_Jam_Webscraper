#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int Pancakes(string S,int K)
{
	int counter = 0;
	for(int i=0;i<S.length();++i)
	{
		if(S[i] == '-')
		{
			for(int j=i;j<=i+K-1;++j)
			{
					if(j>=S.length())
					{
						return -1;
					}
					S[j] = S[j] == '+' ? '-' : '+';
					
			}
			counter++;
		}
	}
	for(int i=0;i<S.length();++i)
	{
		if(S[i] != '+')
		{
			counter = -1;
			break;
		}
	}

	return counter;
}


int main()
{
	int testcase;
	int K;
	string S;
	cin>>testcase;
	int counter = 1;
	while(testcase--)
	{
		cin>>S;
		cin>>K;
		cout<<"Case #"<<counter++<<": ";
		int ans = Pancakes(S,K);
		if(ans < 0)
			cout<<"IMPOSSIBLE";
		else
			cout<<ans;
		cout<<"\n";
	}
	return 0;
}