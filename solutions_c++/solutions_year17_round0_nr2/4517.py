#include<iostream>
using namespace std;
int main()
{
	freopen ("B-large.in","r",stdin);
	freopen ("mylarge.txt","w",stdout);
	int t;
	cin>>t;
	int t1=1;
	while(t--)
	{
		string s;
		cin>>s;
		int k=s.size();
		bool fl=true;
		int j;
		int kk;
p1:		for(int i=0;i<k-1;i++)
		{
			if(s[i]>s[i+1])
			{
				s[i]--;
				j=i;
				kk=s[i];
				fl=false;
				break;
			}
		}
		if(fl==false)
		{
			for(int i=j+1;i<k;i++)
			s[i]='9';
			if(j>0&&s[j]<s[j-1])
			{
				fl=true;
				goto p1;
			}
		}
		bool flag=false;
		int j1;
		for(int i=0;i<k;i++)
		{
			if(s[i]!='0')
			{
				flag=true;
				j1=i;
				break;
			}
		}
		cout<<"Case #"<<t1<<": ";
		t1++;
		for(int i=j1;i<k;i++)
		cout<<s[i];
		cout<<endl;
	}
}
