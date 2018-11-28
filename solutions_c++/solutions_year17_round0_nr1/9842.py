#include <iostream>
using namespace std;
#include <string>
#include <fstream>


int flips(string str,int k)
{
	int count=0,i,j;
	for(i=0;str[i]!='\0';i++)
	{
		if(str[i]=='+')
		{
		count++;	
		}
	}
	int len=i;
		
	if(count==i)
	return 0;
	else
	{
		count=0;
	for(i=0;i<len-k+1;i++)	
	{
		if(str[i]=='-')
		{
			count++;
			for(j=i;j<(i+k) && j<len;j++)
			{
				if(str[j]=='-')
				{
				str[j]='+';	
				}
				else
				{
				str[j]='-';		
				}
			}
		}
	}
		for(i=0;i<len;i++)	
		{
		if(str[i]=='-')
		{
			return -1;
		}
		}


	return count;
	}
	
	
}


int main()
{
	int t,k;
	string str;
	cin>>t;
	int i=0;
	int *arr=new int[t];
while(i<t)
{
	cin>>str;
	cin>>k;
	
	arr[i]=flips(str,k);
	i++;
	
}
i=0;



while(i<t)
{
	if(arr[i]==-1)
cout<<"Case #"<<i+1<<":"<<" "<<"IMPOSSIBLE"<<endl;
else
cout<<"Case #"<<i+1<<":"<<" "<<arr[i]<<endl;

i++;

}

	
	return 0;
}
