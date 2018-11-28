#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,a1=0;
	cin>>t;
	while(t--)
	{
		a1++;
		int i=0;
		string s1;
		cin>>s1;
		int k;
		cin>>k;
		for(int j=0;j<=s1.size()-k;j++)
		{
			if(s1[j]=='-')
			{
				i++;
				for(int l=0;l<k;l++)
				{
					if(s1[j+l]=='-')
						s1[j+l]='+';
					else
						s1[j+l]='-';
				}
			
			}
		}
		int parity=0;
		for (int s=0;s<s1.size();s++)
		{
			if(s1[s]=='-')
				parity=1;
		}
		if(parity)
		{
			cout<<"CASE #"<<a1<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"CASE #"<<a1<<": "<<i<<endl;
		}
	}
	
	return 0;
}
