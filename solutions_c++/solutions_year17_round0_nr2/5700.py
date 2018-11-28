#include <bits/stdc++.h>
using namespace std;
int check(long long s)
{
    long long x,y;
while(s>=10)
{
    x=s%10;
    s=s/10;
    y=s%10;
    if(x<y)
    return -1;
}
	return 0;
}
int main()
{
	
	long long x,t,T,len1,ind;
	string s;
	cin>>T;
	t=1;
	while(T--)
	{
			x=0;
		cin>>s;
		long long len=s.length();
		for(long long i=len-1,j=0;i>=0;i--,j++)
		{
			x+=(s[i]-'0')*pow(10,j);
		}
		if(check(x)==0)
		{
			cout<<"Case #"<<t<<": "<<x<<endl;
		}
		else
		{
			ind=0;
			len1=len;
			for(long long k=len-1;k>0;k--)
			{
				s[k]='9';
				len1--;
				for(int j=s[k-1]-'0'-1;j>0;j--)
				{
					s[k-1]=j + '0';
					x=0;
					for(long long i=len1-1,j=0;i>=0;i--,j++)
					{
						x+=(s[i]-'0')*pow(10,j);
					}
				//	cout<<"Value of x  and s[k-1] now is"<<x<<" "<<s[k-1]<<endl;
					if(check(x)==0)
					{
						cout<<"Case #"<<t<<": "<<s<<endl;
						ind=-1;
						break;
					}	
				}
				if(ind==-1)
					break;
				if(k==1)
				{
					x=0;
					for(long long i=len-1,j=0;i>0;i--,j++)
					{
						x+=(s[i]-'0')*pow(10,j);
					}
					cout<<"Case #"<<t<<": "<<x<<endl;
					break;
				}
			}
		}
		t++;
	}

}