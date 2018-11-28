#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	cin>>T;
	string S;
	int K;
	
	for(int i=1;i<=T;i++)
	{
		cin>>S>>K;
		int flips = 0;
		for(int p = K; p>=1; p--)
		{
			for(int q = 0; q < S.length()-p; q++)
			{
				string temp = S.substr(q,p);
				//cout<<temp<<"\n";
				if(count(temp.begin(), temp.end(), '-') == p && q+K<=S.length())
				{
					++flips;
					for(int r = 0; r < K; r++)
					{
						char c = S[q+r];
						if(c=='-')
							c='+';
						else
							c = '-';
						S[q+r]=c;
					
					}
				}
			}
		}
		//cout<<S<<"\n";
		if(count(S.begin(),S.end(),'+') == S.length())
		{
			cout<<"Case #"<<i<<": "<<flips<<"\n";
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
		}
		
	}
}
