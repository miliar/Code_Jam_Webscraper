#include <bits/stdc++.h> 
using namespace std;
#include <fstream> 

int main()
{	
	   freopen("A-small-attempt0.in","r",stdin);
    freopen("s1.out","w",stdout);

	long long int t,n=0,k;
	string s,s1;
	cin>>t;
	for(long long int i=0;i<t;i++)
	{		

		cin>>s>>k;
		s1=s;
			n=0;
		cout<<"Case #"<<i+1<<": ";

		
		
		int c=0,d=0;

		for (int j = 0; j < s.size()-k+1; j++)
		{
			if(s[j]=='-')
			{
				for (int p = 0; p < k; p++)
				{
					if(s[j+p]=='-')
						s[j+p]='+';
					else
						s[j+p]='-';
				}
				c++;    
			}	


			/*if(s1[z]=='-')
			{
				for (int p = 0; p<4; p++)
				{
					if(s1[z-p]=='-')
						s1[z-p]='+';
					else
						s1[z-p]='-';
				}
				d++;
			}	*/
		}
		int q=0;

		for (int p = 0; p <k; p++)
				{
					if(s[s.size()-1-p]=='+')
						q++;
				}
				if(q==k)
		cout<<c<<endl;
	else
		cout<<"IMPOSSIBLE"<<endl;




	}
			


	
return 0;				
				
}
		
	