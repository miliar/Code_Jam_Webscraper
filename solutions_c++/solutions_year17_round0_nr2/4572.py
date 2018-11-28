#include<bits/stdc++.h>
using namespace std;

unsigned long long int ll;
char a[50],s[50];

int main()
{
/*	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
*/	int test;
	cin>>test;
	for(int tt=1;tt<test+1;tt++)
	{
		cin>>a;
		int n=strlen(a);
		int t=1;
		
//		cout<<a<<" ";
		int brk=0;
		for(int it=0;it<20;it++)
		{
			for(int i=n-1;i>brk;i--)
			{
				if(a[i] == '0')
				{
					for(int j=i+1;j<n;j++)
						a[j] = '9';
					while(a[i] == '0' && i>=1)
					{
						a[i]='9';
						i--;
					}
					a[i] --;
					i++;
				}
				else if(a[i-1] > a[i])
				{
					a[i-1]--;
					for(int j=i;j<n;j++)
						a[j] = '9';
				}
			}
			while(a[brk] < '1' || a[brk] > '9')
				brk++;
		}
		
		while(a[brk] < '1' || a[brk] > '9')
			brk++;
		
		cout<<"Case #"<<tt<<": "<<a+brk<<"\n";
	}
}
