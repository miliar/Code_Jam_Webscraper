/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;


int arr[1003];
int arr1[1003];

int main() 
{
	int t;
	scanf("%d",&t);
	for(int r=1;r<=t;r++)
	{
		string s;
		cin>>s;
		for(int i=0;i<s.length();i++)
		{
			arr[i]=s[i]-'0';
			arr1[i]=arr[i];
		}
		int mn=arr1[s.length()-1];
		for(int i=s.length()-2;i>=0;i--)
		{
			if(arr1[i]>mn)
			{
				arr1[i]=arr[i]-1;
				for(int j=i+1;j<s.length();j++)
				{
					arr1[j]=9;
				}
				mn=arr1[i];
				continue;
			}
			mn=min(arr1[i],mn);
		}
		int st=0;
		for(int i=0;i<s.length();i++)
		{
			if(arr1[i]!=0)
			{
				st=i;
				break;
			}
		}
		string ans="";
		for(int i=st;i<s.length();i++)
		{
			ans=ans+(char)(arr1[i]+'0');
		}
		cout<<"Case #"<<r<<": "<<ans<<endl;
	}	
	return 0;
}