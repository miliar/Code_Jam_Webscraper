/*
Google Code Jam 2017/ Qualification Round
Problem B. Tidy Numbers
Author: Borey
*/

#include<bits/stdc++.h>

using namespace std;

int main()
{
	
//	freopen("B-large.in", "r", stdin);
//	freopen("b-large-output.in", "w", stdout);
	
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		string input;
		cin>>input;		
		int size = input.length();
		int num[size];
		for(int i=0;i<size;i++)
		{
			num[i] = (int)(input[i]-'0');
		}
		
		for(int i=size-2;i>=0;i--)
		{
			if(num[i] > num[i+1])
			{
				for(int j=i+1;j<size;j++)
				{
					num[j] = 9;
				}
				if(num[i]-1 >=0)
				{
					num[i] = num[i] - 1;
				}
			}
		}
				
		cout<<"Case #"<<T<<": ";
		bool not_zero = false;
		for(int i=0;i<size;i++)
		{
			if(num[i] != 0) not_zero = true;
			if(not_zero) cout<<num[i];
		}
		cout<<endl;	
	}
	return 0;
}
