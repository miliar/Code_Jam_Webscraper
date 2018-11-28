#include<iostream>

using namespace std;
int main()
{
	freopen("input_file_name.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int *arr,i,j,t,count,temp,index;
	long n;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		f:
		temp=n;
		count=0;
		while(temp!=0)
		{
			count++;
			temp=temp/10;
		}
		index=count;
		arr=new int(count);
		temp=n;
		while(temp!=0)
		{
			arr[--index]=temp%10;
			temp=temp/10; 
		}
		for(j=0;j<count-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				n--;
				goto f;
			}	
		}
		cout<<"Case #"<<i+1<<": "<<n<<endl;
		
	}
	return 0;
}
