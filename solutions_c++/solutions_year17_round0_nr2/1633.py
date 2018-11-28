#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T,N; cin>>T;
	string num;
	for (int t=1;t<=T;t++)
	{
		cin>>num;
		N=num.size();
		for (int i=1;i<N;i++)
		{
			if (num[i-1]>num[i])
			{
				for (int j=i;j<N;j++) num[j]='9';
				bool s=true;
				for (int j=i-1;s&&j>0;j--)
				{
					if (--num[j]<num[j-1]) num[j]='9';
					else s=false;
				}
				if (s&&--num[0]=='0') num=num.substr(1,N-1);
				break;
			}
		}
		cout<<"Case #"<<t<<": "<<num<<endl;
	}
}
