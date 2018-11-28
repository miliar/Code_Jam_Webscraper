#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for (int i = 1; i <= n; ++i)
	{
		string input;
		cin>>input;
		int len=input.length();
		int c=0;
		if(len==1)
		{
			cout<<"Case #"<<i<<": "<<input<<endl;
			continue;
		}
		bool flag=true;
		for (int j = 1; j < len; ++j)
		{
			if(input[j]>input[j-1])
				c=j;
			else if(input[j]<input[j-1])
			{
				flag=false;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(c==len-1 || flag)
		{
			cout<<input<<endl;
			continue;
		}
		for (int j = 0; j <c; ++j)
		{
			cout<<input[j];
		}
		if(input[c]!='1')
			cout<<(char)(input[c]-1);
		for (int j = c+1; j < len; ++j)
		{
			cout<<9;
		}
		cout<<endl;
	}
	return 0;
}