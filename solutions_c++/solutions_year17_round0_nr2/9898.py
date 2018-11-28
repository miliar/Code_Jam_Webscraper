#include<iostream>
#include<fstream>
#include<string.h>
//#include<conio.h>
using namespace std;

int main(){
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("tidynum_small","w",stdout);
	int i=1,t,l,p,arr[19],brr[19];
	cin>>t;
	long long int n;
	while(t--)
	{
		cin>>n;
		int j=0;
		while(n>0)
		{
			arr[j]=n%10;
			n=n/10;
			j++;
		}
		int x=0;
		
		for(l=j-1;l>=0;l--) 
		 brr[j-l-1]=arr[l];
		 
		for(l=0;l<j-1;l++)
		{
			if(brr[l]>brr[l+1])
			x=-1;
		}
		if(x==0)
		{
			cout<<"Case #"<<i<<": ";
			i++;
			if(brr[0]!=0)
		  	 cout<<brr[0];
			for(l=1;l<j;l++)
			 cout<<brr[l];
			 cout<<endl;
			continue;
		}
		l=j-1;
		int temp=0,flag;
		while(l>0)
		{
			flag=0;
			for(p=0;p<l;p++){
				if(brr[l]<=brr[p]){
					arr[l]=9;
					temp=-1;
					flag=-1;
					break;
				}
			}
			if(flag!=-1 && temp==-1){
				arr[l]=brr[l]-1;
				temp=0;
			}
			else if(flag!=-1 && temp==0)
			{
				arr[l]=brr[l];
			}
			l--;
		}
		if(temp==-1)
		 arr[0]=brr[0]-1;
		else if(temp==0)
		 arr[0]=brr[0];
		for(l=0;l<j-1;l++)
		{
			if(arr[l]==9)
			{
				while(l<j)
				arr[l++]=9;
			}
		}
		
		cout<<"Case #"<<i<<": ";
		i++;
		
		
		
		if(arr[0]!=0)
		cout<<arr[0];
		for(l=1;l<j;l++)
		cout<<arr[l];
		cout<<endl;
		
	}
	return 0;
//	getch();
}
