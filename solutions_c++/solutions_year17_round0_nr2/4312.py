#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		string N;
		cin>>N;
		int j = 0;
		while(j!=N.size()-1)
		{
			for(j=0; j<N.size()-1;j++)
			{
				if(N[j]>N[j+1])
				{
					break;
				}
			}
			if(j!=N.size()-1)
			{
				int k = j;
				N[k] = N[k]-1;
				k = j+1;
				for(;k<N.size();k++)
				{
					N[k] = '9';
				}
			}
		}
		for(j=0;j<N.size();j++)
		{
			if(N[j]!='0')
				break;
		}
		size_t a = j;
		int b = j;
		string answer(N.size()-a,'0');
		for(j=0;j<answer.size();j++)
		{
			answer[j] = N[j+b];
		}

		cout<<"Case #"<<i<<": "<<answer<<endl;
	}
}