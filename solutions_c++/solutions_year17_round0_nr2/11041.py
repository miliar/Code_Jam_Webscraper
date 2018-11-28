#include <bits/stdc++.h>
//number to string conversion
using namespace std;
template <typename T>
string NumberToString(T pNumber)
{
 ostringstream oOStrStream;
 oOStrStream << pNumber;
 return oOStrStream.str();
}


//checking strings
int traverse_check(string s)
{
	for(int i =1;i<s.length();i++)
	{
		if(s[i-1]>s[i])
		{
			return 0;
		}
	}
	return 1;
}

int main()
 {
    ifstream cin("B-small-attempt0.in");
    ofstream cout("output.txt");
	int t,restore;
	long long int a,result=0,m;
	cin>>t;
	m=t;
	while(t--)
	{
	string s;
	cin>>s;
	a=atoi(s.c_str());
	for(int i=a;i>=0;i++)
	{
		restore=traverse_check(s);
		if(restore==1)
		{
			result=a;
			break;
		}
		else{
			a=a-1;
			s=NumberToString(a);
		}
	}
	
	cout<<"Case #"<<m-t<<": "<<result<<endl;	
    }
    
}
