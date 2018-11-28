#include<iostream>
#include <string.h>
using namespace std;
int main()
{
	int t;
	char s[1001];
	cin>>t;
	for(int i =1;i<=t;i++)
	{
		int ans = 0, check = 1, k;
		cin>>s>>k;
		int length = strlen(s);
		for(int j=0;j<length;j++)
		{
			if( s[j] != '+')
			{
				if( j<= length - k )
				{
					s[j] = '+';
					for( int it = j+1; it<j+k; it ++ )
						s[it] = (s[it]=='+')?'-':'+';
					
					ans++;
				}	
				else
				{
					check = 0;
					break;
				}
			}
		}
		if(check)
			cout<<"Case #"<<i<<": "<<ans<<endl;
		else
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}