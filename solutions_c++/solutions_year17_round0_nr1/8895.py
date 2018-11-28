#include<iostream>
#include<fstream>
using namespace std;

int check(string s ,int n,int k,int i ,int c)
{
	if(i==n && s[i] == '+')
	{
		return c;
		
	}
	if(i> n-k)
	{
		for(int j = n-k+1;j<n;j++)
		{
			if(s[j] == '-')
			return -1;
		}
		return c;
	}
	if(s[i] == '+')
	{
		return check(s,n,k,i+1,c);
	}
	if(s[i] == '-')
	{
		for(int j=i;j< i+k;j++)
		{
			if(s[j] == '-')
			s[j] = '+';
			else
			s[j]='-';
			
		}
		
		//cout<<s<<" "<<c<<"   "<<endl;
		return check(s,n,k,i+1,c+1);
	}
}

int main()
{
	ifstream myfile;
	myfile.open("A-input.in");
	ofstream urFile;
    urFile.open("ans.out");
int i=1;
    int t;
    myfile>>t;
    while(t--)
    {
	string s;
	int k;
	myfile>>s>>k;
	int n = s.size();
	
	int c = check(s,n,k,0,0);
	if(c==-1)
	urFile<<"Case #"<<i++<<": "<<"IMPOSSIBLE"<<endl;
	else
	urFile<<"Case #"<<i++<<": "<<c<<endl;
}
	return 0;
}
