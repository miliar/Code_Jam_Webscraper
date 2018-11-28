#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		string s,s1,s2,s3;
		long long int a,b,i,j,c=0;
		vector<string>v;
		cin>>s1;
		s=s1;
		sort(s1.begin(),s1.end());
		stringstream ss;
		ss<<s;
		ss>>a;
		stringstream ss1;
		ss1<<s1;
		ss1>>b;
		b=max(b,a-b);
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='0'||s[i]=='1')
			c++;
		}
		if(c==s.length())
		cout<<b<<endl;
		else
		{
     	for(i=b;i<=a;i++)
		{
		s2=to_string(i);
		s3=s2;
		sort(s2.begin(),s2.end());
		if(s3==s2)
		v.push_back(s2);
		}
		cout<<v[v.size()-1]<<endl;
		}
		
	}
	return 0;
}