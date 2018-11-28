#include<iostream>

using namespace std;

int istidy(int x)
{
	int t=1, a, b;
	while(x>9)
	{
		a=x%10;
		x=x/10;
		b=x%10;
		if(a<b)
		{
			t=0;
			break;
		}
	}
	return t;
}

int main()
{
	int T, N, t, i;


	cin>>T;
	for(i=1;i<=T;++i)
	{
		cin>>N;
		for(;N>0;--N)
		{
			t=istidy(N);
			if(t==1)
			{
				cout<<"Case #"<<i<<": "<<N<<endl;
				break;
			}
		}
	}
}
