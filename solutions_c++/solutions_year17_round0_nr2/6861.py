#include<iostream>
#include<string.h>

using namespace std;

FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);

char s[30];
int a[30];

int findmax(int k)
{	
	int max=0;
	for(int i=0;i<k;i++)
	{
		if(a[i]>max)
			max=a[i];
	}
	return max;
}

int checksort(int f)
{
	for(int i=0;i<f-1;i++)
	{
		if(a[i+1]<a[i])
			return 0;
	}

	return 1;
}

int main()
{
	long int t3,x;

	cin>>t3;
	x=t3;

	while(x--)
	{	
		cin>>s;

		int i,max,pos;

		int f=strlen(s);

		if(f==1)
		{
			cout<<"Case #"<<t3-x<<": "<<s[0]<<endl;
			continue;
		}

		for(i=0;s[i]!='\0';i++)
			a[i]=s[i]-48;

		if(checksort(f)==1)
		{
			cout<<"Case #"<<t3-x<<": "<<s<<endl;
			continue;
		}

		int t=f,t1;

		while(t>=0)
		{
			for(i=0;i<t;i++)
			{
				if(a[i]==findmax(t))
					break;
			}

			t1=i;

			a[i]=a[i]-1;

			for(i++;i<t;i++)
				a[i]=9;

			if(checksort(f)==1)
			{
				//long long int y=0;
				//for(int i=0;i<f;i++)
					//y=(y*10)+a[i];
				cout<<"Case #"<<t3-x<<": ";

				i=0;

				if(a[0]==0)
					i=1;

				for(;i<f;i++)
				{	
					cout<<a[i];
				}
				cout<<endl;
				break;
			}

			t=t1+1;

		}


	}
}