


#include<iostream>
#include<cstdlib>
using namespace std;
int store[1000],track=0;

int check(int m)
{
	if(m/10==0)
	{
		return 1;
	}
	
	char no[1000];
	itoa(m,no,10);
	int flag=1;
	for(int i=1;no[i]!=NULL;i++)
	{
		if((no[i]-'0')<(no[i-1]-'0'))
		{
			flag=0;
			break;
		}
	}
	return flag;
}

int main()
{
	freopen("B-small-attempt3.in","r",stdin);
   freopen("output_file_name.out","w",stdout);

	
	
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int a;
		cin>>a;
		TOP:
		if(check(a)==0)
		{
			a--;
			goto TOP;
		}
		store[track]=a;
		track++;
	}
	for(int i=0;i<track;i++)
	{
		cout<<"Case #"<<i+1<<": "<<store[i]<<endl;
	}
}