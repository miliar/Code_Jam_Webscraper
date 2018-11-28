/*
Google Code Jam 2017/ Qualification Round
Problem A. Oversized Pancake Flipper
Author: Borey
*/

#include<bits/stdc++.h>

using namespace std;

int main()
{
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out","w", stdout);
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{		
		string s;
		cin>>s;
		int k;
		cin>>k;
		
		int size = s.length();
		long time = 0;
		int i = 0;
		for(i=0;i<=size-k;i++) //check index [size-k] is the last case
		{
			if(s[i]=='-')
			{
				time++;
				//change side
				for(int j=i;j<i+k;j++)
				{
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		//check from the last if there is at least '-' that mean "IMPOSSIBLE"
		for(i=1;i<k;i++)
		{
			if(s[size-i]=='-')
			{
				time = -1;
				break;	
			}
			
		}
		if(time == -1) cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<t<<": "<<time<<endl;

	}
	return 0;
}
