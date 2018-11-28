#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
   int t;
   cin>>t;
   for (int p = 0; p < t; p++)
   {
		string s;
		cin>>s;
		bool flag = s[0] == '9' ? true : false;
		for (int i = s.length() - 2; i >= 0; i--)
		{
		
			    if (s[i] > s[i + 1])
			    {
			    	s[i + 1] = '9';
			    	if (s[i] > '0')
			    		s[i]--;
			    }
			    int k = i + 1;
			    while ( k < s.length() - 1 && s[k] > s[k + 1])
			    {
			    	s[k + 1] = '9';
			    	k++;	
			    } 
			    
		}

		if (s[0] > '0')
		{
			cout<<"Case #"<<p + 1<<": "<<s<<endl;
		}
		else
		{
			cout<<"Case #"<<p + 1<<": ";
			for (int i = 0; i < s.length() - 1; i++)
			{
				cout<<"9";
			}
			cout<<endl;
		}
   }   
   return 0;
}
