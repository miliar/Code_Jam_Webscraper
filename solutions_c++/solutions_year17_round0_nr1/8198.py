#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int arr[t];
	for(int i=0;i<t;i++)
	{
		int k;
		string s;
		cin>>s>>k;
		int l=s.length();
		int count=0;
		for(int j=0;j<=l-k;j++)
		{
			if(s[j]=='-')
			{
				count++;
				for(int n=j;n<j+k;n++)
				if(s[n]=='-') s[n]='+';
				else s[n]='-';
			}
		}
		int c=0;
		for(int j=l-k;j<l;j++)
		if(s[j]=='-') 
		{
			c=1;
			arr[i]=-1;
			break;
		}
		if(c==0) arr[i]=count;
	}
	for(int i=0;i<t;i++)
	{
		if(arr[i]==-1)  cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<(i+1)<<": "<<arr[i]<<endl;
	}
	return 0;
}
