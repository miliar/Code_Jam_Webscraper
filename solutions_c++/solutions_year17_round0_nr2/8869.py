#include<cstdio>
#include<iostream>
#include<string.h>
#include<bits/stdc++.h>
using namespace std;
int mastercount=0;
char subtract(char a[], int i)
{
	int l=strlen(a);
	
	int n;
	//cout<<a[0]<<" "<<a[1]<<endl;
	
		if(a[i]>48)
			{
				n=(int)(a[i]);
				//cout<<n;
				n--;
				a[i]=n;
				
			}
		else if(a[i]==48)
		{
		
			if(l==1)
				a[i]=-1+48;
			else{
			
				a[i]=48+9;
				subtract(a, i-1);
			}
		}
		
		if(a[0]==48)
		{	
			for(int i=1;i<=n;i++)
			{
				a[i-1]=a[i];
			}
		}
		
		
		//cout<<"apple"<<mastercount++;
}
int main()
{
	int t, rem, last, i;
	char num[20];
	cin>>t;
	char a[101][100];
	for(i=0;i<t;i++)
	{
		cin>>a[i];
	}

	for(int z=0;z<t;z++)
	{
		strcpy(num,a[z]);
		
		int l=strlen(num);
		for(int i=1;i<l;i++)
		{
			
			if(num[i]>=num[i-1])
				continue;
			else
			//if(num[i]<num[i-1])
			{
				int k=i;
				while(k<l)
				{
					num[k]=48;
					k++;
				}
				//<<num<<"\n";
				//
				subtract(num,l-1);
				//strcpy(num,subtract(num,l-1));
				l=strlen(num);
				//cout<<num<<"   "<<i<<endl;
				i=i-2;
			}
		}
		
		cout<<"case #"<<z+1<<": "<<num<<endl;
	}//end of test case loop
	return 0;
	
}

	
