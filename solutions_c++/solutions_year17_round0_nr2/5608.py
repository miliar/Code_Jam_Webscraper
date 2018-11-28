#include<iostream>
using namespace std;
int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int tc;
	cin>>tc;
	int j=1;
	while(tc--)
	{
	string str;
	cin>>str;
	while(true)
	{
	for(int i=0;i<str.length()-1;i++)
	{
		if(str[i]>str[i+1])
		{
			str[i]=str[i]-1;
			for(int j=i+1;j<str.length();j++)
			str[j]='9';
			break;
		}
	}
	int i;
	for( i=0;i<str.length()-1;i++)
	{
		if(str[i]>str[i+1])
		break;
	}
	if(i==str.length()-1)
	break;
    }
    cout<<"Case #"<<j<<": ";
    j++;
	for(int i=0;i<str.length();i++)
	{
		if(str[i]!='0')
		cout<<str[i];
	}
	cout<<endl;
}
fclose(stdout);
}