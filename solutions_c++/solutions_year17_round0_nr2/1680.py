#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("l.txt","wb",stdout);
	int data;
	scanf("%d",&data);
	for(int p=1;p<=data;p++)
	{
		string s;
		cin>>s;
		int las=0;
		for(int i=0;i<int(s.size())-1;i++)
		{
			if(s[i]>s[i+1])
			{
				string ans;
				for(int j=0;j<las;j++)ans.push_back(s[j]);
				if(las!=0||s[las]!='1')ans.push_back(s[las]-1);
				for(int j=las+1;j<s.size();j++)ans.push_back('9');
				s=ans;
				break;
			}
			else if(s[i]<s[i+1])las=i+1;
		}
		printf("Case #%d: ",p);
		cout<<s<<endl;
	}
}