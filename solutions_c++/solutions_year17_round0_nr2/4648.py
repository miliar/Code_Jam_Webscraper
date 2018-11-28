#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	int t,i,j,k=1,len;
	string s;
	cin>>t;
	while(k<=t)
	{
		cin>>s;
		int flag=0;
		while(flag==0)
		{
			len=s.length();
			i=1;
			while(i<len && s[i]>=s[i-1])
				i++;
			if(i!=len)
			{
				j=i-1;
				if(s[i-1]=='1')
				{
					
					while(j>=1 && s[j]=='1')
						j--;
				}
				s[j]--;
				i=j+1;
				while(i<len)
				{
					s[i]='9';
					i++;
				}
			}
			else
			{
				flag=1;
			}
			i=0;
			while(i<len-1 && s[i]=='0')
				i++;
			s=s.substr(i);
			
		}
		cout<<"Case #"<<k<<": ";
		
		cout<<s<<endl;
		k++;
	}
}
