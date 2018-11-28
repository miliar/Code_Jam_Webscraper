#include <iostream>
using namespace std;

string getNumString(long long int N)
{
	string s = "";
	while(N != 0) 
	{ 
		char c = (N%10 + '0');
		s = c + s;
		N /= 10;
	}
	return s;
}

string getNext(string s)
{
	if(s.length() == 0 || s == "0")return "";
	int i,j;
	int len = s.length();
	bool flag = false;
	for(i=0;i<len-1;i++)
	{
		if(s[i] > s[i+1])
		{
			j = i;
			s[i++]--;
			flag = true;
			break;
		}
	}
	if(flag)
	{
		while(i < len)
		{
			s[i] = '9';
			i++;
		}
		return getNext(s.substr(0,j+1)) + s.substr(j+1, s.length()-j-1);
	}
	return s;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	long long int N;
	for(int i=1;i<=T;i++)
	{
		cin>>N;
		cout<<"Case #"<<i<<": "<<getNext(getNumString(N))<<"\n";
	}		
}
