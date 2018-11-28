#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;




int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("A-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		string s;
		int K;
		cin>>s>>K;
		int ans=0;
		for (int i=0; i+K-1<s.length(); i++)
		{
			if (s[i]=='-')
			{
				for (int j=i; j<=i+K-1; j++)
				{
					if (s[j]=='-')
					{
						s[j]='+';
					}
					else
					{
						s[j]='-';
					}
				}
				ans++;
			}
		}
		
		bool ok=true;
		for (int i=0; i<s.length(); i++)
		{
			if (s[i]=='-')
			{
				ok=false;
			}
		}
		if (ok==true)
		{
			cout<<"Case #"<<cnt<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<cnt<<": IMPOSSIBLE"<<endl;
		}
		
	}
	
	
	
	
	return 0;
	
}
