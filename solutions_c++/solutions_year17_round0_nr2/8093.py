#include <bits/stdc++.h>
using namespace std;



int main()
{

	int t,i,cases;

	cin>>t;
	cases=1;
	while(t--)
	{
		int cnt=0;
		string s,temp;
		int marker = 0;
		int marker2 = 0;

		cin>>s;
		temp = s;
		cout<<"Case #"<<cases<<": ";
		cases+=1;
		if(s.length()==1)
		{
			cout<<s;
		}

		else
		{

			for(i=1;s[i]!='\0';i+=1)
			{
				if(s[i]>=s[i-1])
				{
					marker = i; 
				}
				else
				{
					break;
				}
			}
			if(marker==s.length()-1)
			{
				cout<<s;
			}

			else
			{
				for(i=marker+1;s[i]!='\0';i+=1)
				{
					s[i]='9';
				}

				s[marker]-=1;
				for(i=marker-1;i>=0;i--)
				{
					
					if(s[i]>s[i+1])
					{
						s[i]-=1;
					}
				}

				for(i=0;i<=marker;i+=1)
				{
					if(s[i]=='0')
						cnt+=1;
				}
				
				if(cnt==marker+1)
				{
					for(i=0;i<s.length()-1;i+=1)
						cout<<9;
				}
				else
				{
					for(i=0;s[i]!='\0';i+=1)
					{
						if(s[i]=='0')
						{}
						else
							{marker2=i;break;}
					}
					for(i=0;s[i]!='\0';i+=1)
					{
						if(s[i]<temp[i])
						{
							for(int j=i+1;s[j]!='\0';j+=1)
								s[j]='9';
							break;
						}
					}
					for(i=marker2;s[i]!='\0';i+=1)
					{
						cout<<s[i];
					}
				}
			}

		}
		cout<<endl;
	}


	return 0;
}