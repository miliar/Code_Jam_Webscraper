#include<iostream>
using namespace std;
int main()
{
	freopen ("input.cpp","r",stdin);
	freopen ("output.cpp","w",stdout);
	int t;
	cin>>t;
	int j=1;
	while(t--)
	{
	string s;
	cin>>s;
	while(true)
	{
	for(int i=0;i<s.length()-1;i++)
	{
		if(s[i]>s[i+1])
		{
			s[i]=s[i]-1;
			for(int j=i+1;j<s.length();j++)
			s[j]='9';
			break;
		}
	}
	int i;
	for( i=0;i<s.length()-1;i++)
	{
		if(s[i]>s[i+1])
		break;
	}
	if(i==s.length()-1)
	break;
    }
    cout<<"Case #"<<j<<": ";
    j++;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!='0')
		cout<<s[i];
	}
	cout<<endl;
}
fclose(stdout);
}
