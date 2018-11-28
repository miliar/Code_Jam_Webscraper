#include<iostream>
#include<algorithm>
using namespace std;
int a[20];
long long int b;
int numa;
int main()
{
	int test;
	cin>>test;
	for(int index=1;index<=test;++index)
	{
		numa=0;
		cin>>b;
		long long int r=b;
		while(r>0)
		{
			a[numa]=r%10;
			numa++;
			r/=10;
		}
		int pistol=0;
		int pos=0;
		bool flag=true;
		for(int i=numa-1;i>=0;--i){
			if(a[i]<pistol){
				flag=false;
				break;	
			} 
			else if(a[i]>pistol){
				pos=i;
				pistol=a[i];
			}
		}
		cout<<"Case #"<<index<<": ";
		if(flag){
			cout<<b;
		}
		else if(pistol==1)
		{
			for(int i=numa-2;i>=0;--i) cout<<9;
		}
		else{
			for(int i=numa-1;i>pos;--i){
				cout<<a[i];
			}
			cout<<a[pos]-1;
			for(int i=pos-1;i>=0;--i){
				cout<<9;
			}
		}
		cout<<endl;
	}
	return 0;
}
