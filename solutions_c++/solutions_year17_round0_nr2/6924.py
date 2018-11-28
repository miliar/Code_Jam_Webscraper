#include<bits/stdc++.h>
using namespace std;

void swap(int *a,int *b)
{
	int temp=*a;
	*a=*b;
	*b=temp;
}
	

int main()
{
	long long int t,t1,pos,n;
//	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin>>t1;
	int arr[20];
	for(int t=1;t<=t1;t++){
		
		cin>>n;
		
		int i=0;
		while(n>0){
			arr[i]=n%10;
			n/=10;
			i++;
		}
		//for(int p=0;p<i;p++)
		//	cout<<arr[p]<<" ";
		//cout<<endl;
	
		int j=0,k=i-1,len=i;
				
		while(j<k){
			swap(&arr[j],&arr[k]);
			j++;k--;
		}
		for(i=0;i<len-1;i++)
		{
			if(arr[i+1]<arr[i])
			{	
				int mn;
				for(mn=i;;mn--){
					if(arr[mn]!=arr[mn-1])
					{
						break;
					}
				}
				pos=mn;
				arr[pos]=arr[pos]-1;
				for(int j=pos+1;j<=len;j++)
					arr[j]=9;
				break;
			}
		}
		printf("Case #%d: ",t);
		for(i=0;i<len;i++)
		{
			if(arr[i]!=0)
			printf("%d",arr[i]);
		}
		cout<<endl;
				
				
	}
return 0;
}
