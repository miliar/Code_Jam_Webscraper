#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,x;
	cin>>t;
	x=t;
	while(t--)
	{
		unsigned long long int n,i,j,k;
		string s;
		cin>>s;
		int l=s.length();
		if(l==1)
		cout<<"case #"<<(x-t)<<": "<<s<<endl;
		else
		{
			for(j=0;j<l;j++)
			{
				s[l]='9';
				if(s[j]>s[j+1])
				{
					s[l]='\0';
					if(s[j]=='1' && s[j+1]=='0')
					{
						k=0;
						while(k!=l-1)
						s[k++]='9';
						l--;
						break;	
					}
					else
					{
						if(s[j]!=s[j-1])
						s[j]--;
						else
						{
							while(s[j]==s[j-1]){
							j--;};
							s[j]--;
						}
						for(k=j+1;k<l;k++)
						s[k]='9';
						s[l]='\0';
						break;
					}
					
				}
				else
				continue;
			}
			cout<<"case #"<<(x-t)<<": ";
			for(int q=0;q<l;q++)
			cout<<s[q];
			cout<<endl;
		}
		
	}
	return 0;
}
