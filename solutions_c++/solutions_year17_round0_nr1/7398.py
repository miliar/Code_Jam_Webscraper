#include<iostream>
#include<string>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		string cakes;
		int k, ans=0;
		cin>>cakes>>k;
		for (size_t j=0;j<=cakes.length()-k;j++)
		{
			if (cakes[j]=='-')
			{
				ans++;
				for (int l=0;l<k;l++)
					cakes[j+l] = (cakes[j+l]=='+')?'-':'+';
			}
		}
		if (cakes.find('-') == string::npos)
			cout<<"Case #"<<i<<": "<<ans<<endl;
		else
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
