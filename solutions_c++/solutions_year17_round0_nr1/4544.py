#include<iostream>
using namespace std;
int main()
{
	freopen ("A-large.in","r",stdin);
	freopen ("Aoutlarge.txt","w",stdout);
	int t;
	cin>>t;
	int t1=1;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		int cnt=0;
		int len=s.size();
		for(int i=0;i<=len-k;i++)
		{
			//cout<<i<<" ";
			if(s[i]=='-')
			{
				cnt++;
				for(int j=i;j<i+k;j++)
			    {
				    if(s[j]=='+')s[j]='-';
				    else s[j]='+';
			    }
			}
			else continue;
			//cout<<s<<endl;
		}
		bool fl=true;
		for(int i=0;i<=len;i++)
		{
			if(s[i]=='-')
			{
				fl=false;
				break;
			}
		}
		if(fl)
		{
			cout<<"Case #"<<t1<<": ";
		t1++;
		cout<<cnt<<endl;
		
		}
		else
		{
			cout<<"Case #"<<t1<<": ";
		t1++;
		cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
