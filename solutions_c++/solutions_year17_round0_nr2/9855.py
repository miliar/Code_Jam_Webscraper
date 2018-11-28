#include<iostream>
#include<fstream>
#include<string.h>
//#include<conio.h>
using namespace std;

int main(){
	
	freopen("B-small-attempt2.in","r",stdin);
	freopen("tidyrealsmallimp","w",stdout);
	int i,t,l,p,a[19],b[19];
	cin>>t;
	long long int n;
	for(i=1;i<=t;i++){
		cin>>n;
		int j=0;
		while(n>0){
			a[j++]=n%10;
			n=n/10;
		}
		int x=0;
		for(l=j-1;l>=0;l--) b[j-l-1]=a[l];
		for(l=0;l<j-1;l++){
			if(b[l]>b[l+1])
			x=-1;
		}
		if(x==0){
			cout<<"Case #"<<i<<": ";
			if(b[0]!=0)
			cout<<b[0];
			for(l=1;l<j;l++)
			cout<<b[l];
			cout<<endl;
			continue;
		}
		l=j-1;
		int temp=0,flag;
		while(l>0){
			flag=0;
			for(p=0;p<l;p++){
				if(b[l]<=b[p]){
					a[l]=9;
					temp=-1;
					flag=-1;
					break;
				}
			}
			if(flag!=-1 && temp==-1){
				a[l]=b[l]-1;
				temp=0;
			}
			else if(flag!=-1 && temp==0){
				a[l]=b[l];
			}
			l--;
		}
		if(temp==-1)
		a[0]=b[0]-1;
		else if(temp==0)
		a[0]=b[0];
		for(l=0;l<j-1;l++){
			if(a[l]==9){
				while(l<j)
				a[l++]=9;
			}
		}
		
		cout<<"Case #"<<i<<": ";
		if(a[0]!=0)
		cout<<a[0];
		for(l=1;l<j;l++)
		cout<<a[l];
		cout<<endl;
	}
	return 0;
//	getch();
}
