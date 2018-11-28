#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int s,k,count;
	string in;
	bool flag;
	cin>>s;
	for(int i=0;i<s;i++)
	{
		cin>>in>>k;
		count = 0;
		flag = false;
		
		for(int j=0;j<=in.length()-k;j++)
		{
			if(in[j]=='-')
			{
				count++;
				in[j] = '+';
				for(int l=1;l<k;l++)
				{
					if(in[j+l]=='+'){in[j+l]='-';}
					else{in[j+l]='+';}
				}
			}
		}
		
		for(int j=in.length()-k;j<in.length();j++){if(in[j]=='-'){flag=true;break;}}
		if(flag){cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;}
		else{cout<<"Case #"<<i+1<<": "<<count<<endl;}
	}
	return 0;
}
