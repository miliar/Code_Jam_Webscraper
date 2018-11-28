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
	
	freopen("B-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		string s;
		cin>>s;
		
		int index=-1;
		for (int i=0; i+1<s.length(); i++)
		{
			if (s[i+1]<s[i])
			{
				index=i;
				break;
			}
		}
		
		if (index==-1)
		{
			cout<<"Case #"<<cnt<<": "<<s<<endl;
		}
		else
		{
			cout<<"Case #"<<cnt<<": ";
			//s[index]--;
			//cout<<s<<endl;
			int index3=0;
			for (int i=index; i-1>=0; i--)
			{
				if (s[i]>s[i-1])
				{
					index3=i;
					break;
				}
			}
			index=index3;
			s[index]--;
			int index2=0;
			if (s[index2]=='0')
			{
				index2++;
			}
			
			for (int i=index2; i<s.length(); i++)
			{
				if (i<=index)
				{					
					cout<<s[i];
				}				
				if (i>index)
				{
					cout<<"9";
				}
			}
			cout<<endl;
		}
	}
	
	
	
	
	return 0;
	
}
