#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t, i, j, flag=0, k, p=0, n,y=0,z=0;
	string s1;
	char a,b;
	cin>>t;
	while(t>0)
	{
		cin>>s1;
		
			if(s1.length()==1)
			{
				cout<<"Case #"<<(++z)<<": "<<s1<<endl;
				
				// cout<<n<<endl;
			}
			else
			{
				while(true)
				{
				for(j=s1.length()-1; j>=0; j--)
				{
					//cout<<s1[j]<<" "<<s1[j-1]<<endl;
					if(s1[j]<s1[j-1])
					{


						s1[s1.length()-p]='9';
						k = s1[s1.length()-p-1]-'0';
						//cout<<k<<endl;
						--k;
						//cout<<"k= "<<k;
						s1[s1.length()-p-1] = '0' + k;
						++p;
						flag=1;


					}
					else
					{
						flag=0;
					}
					if(flag==1)
						break;

				}
				if(flag==0)
					{
						y=-1;
						for(i=0; i<s1.length(); i++)
						{
							if(s1[i]=='0')
							{y=i;
								
							}
							else
							break;
						}
					     ++y;
					     cout<<"Case #"<<(++z)<<": ";
						for(i=y; i<s1.length(); i++)
						{
							cout<<s1[i];
							
						}
					   cout<<endl;
						break;
						}
				
			}
			}

			p=0;
			k=0;
			s1="";
			--t;
		
	}
	return 0;
}