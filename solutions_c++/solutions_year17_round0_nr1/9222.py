#include<iostream>
using namespace std;
int func_check(char arr[],int len);
int main()
{
	int t,m=0;
	cin>>t;
	while(t--)
	{

		m++;
    int  flag=0;
	char arr[1000];
	int k,len;
	cin>>arr;
	cin>>k;
	int i;
	for(i=0;arr[i]!='\0';i++);
	len=i;
    int count=0;
    
    for(int i=0;i<len-k;i++)
    {
        
    	if(arr[i]=='-')
    	{
    		count++;
    		for(int j=i;j<k+i;j++)
    		{
    			if(arr[j]=='-')
    				arr[j]='+';
    			else
    				arr[j]='-';
    		}
    	}
    	
    	if(func_check(arr,len)==1)
    		{
    			cout<<"Case #"<<m<<": "<<count<<endl;
    			flag=1;
    			break;
    			
    		}
    	
    }
    if(flag==0)
    {
        for(int i=len-1;i>=k-1;i--)
    
    {
    	if(arr[i]=='-')
    	{
    		
    		count++;
    		for(int j=i;j>i-k;j--)
    		{
    			
    			if(arr[j]=='-')
    				arr[j]='+';
    			else
    				arr[j]='-';
    		}
    	}
    	
    	if(func_check(arr,len)==1)
    		{
    			cout<<"Case #"<<m<<": "<<count<<endl;
    			flag=1;
    			break;
    			
    		}
    	
    }

}
if(flag==0)
cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
	
}
return 0;
}

int func_check(char arr[],int len)
{
	for(int i=0;i<len;i++)
	{
		if(arr[i]=='-')
			return 0;
	}
return 1;
}