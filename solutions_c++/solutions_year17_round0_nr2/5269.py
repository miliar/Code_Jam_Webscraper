#include <iostream>
using namespace std;

void tidy(int arr[],int i)
{
	
    
    for(int j=0;j<i-1;j++)
    {
        if(arr[j]>arr[j+1])
        {
            arr[j]=arr[j]-1;
            j++;
            while(j<i)
            {
            	arr[j]=9;
            	j++;
            }	
        }
    }

     	int flag=1;
	for(int k=0;k<i-1;k++)
	{
		if(arr[k]>arr[k+1])
		{
			flag=0;
			break;
		}
	}
   if(flag==0)
   	tidy(arr,i);
    
 
}


long long converttoarray(long long  num,int casenum)
{
	long long i=0;
	long long t=num;
	while(t>0)
	{
		i++;
		t=t/10;

	}

    int arr[i];
   t=num;
	for(int j=i-1;j>=0;j--)
	{
		arr[j]=t%10;
		t=t/10;
	}

     tidy(arr,i);


       cout<<"Case #"<<casenum<<": ";

    for(int j=0;j<i;j++)
    {
    	if(arr[j]==0)
    	{

    	}
    	else
    	{
    		cout<<arr[j];
    	}
    }
	
	cout<<endl;

}

int main()
{
       int testcases;
       cin>>testcases;
    int i=1;
       while(testcases--)
       {
       	   long long num;
       	   cin>>num;
           converttoarray(num,i);
           i++;
          
       }
}