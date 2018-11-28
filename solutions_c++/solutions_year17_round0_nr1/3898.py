#include <iostream>
#include <string>
using namespace std;
string trimeer(string input)
{
	int i=0;
	while(i<input.length())
		if(input[i]=='+')
			i++;
		else
			break;
	int j=input.length()-1;
	while(j>=0)
		if(input[j]=='+')
			j--;
		else
			break;
	return input.substr(i,j-i+1);
}
int main()
{
	int n;
	cin>>n;
	for (int j = 1; j <= n; ++j)
	{
		string input;
		cin>>input;
		int k;
		cin>>k;
		int count=0;
		int len=input.length();
		input=trimeer(input);
		if(input.length()==0)
		{
			cout<<"CASE #"<<j<<": 0\n";
			continue;
		}
		while(input.length()>=k)
		{
			for (int i = 0; i < k; ++i)
				input[i]=(input[i]=='-')?'+':'-';
			input=trimeer(input);
			count++;
		}
		if(input.length()>0)
			cout<<"CASE #"<<j<<": "<<"IMPOSSIBLE\n";
		else
			cout<<"CASE #"<<j<<": "<<count<<endl;		
	}
}