#include<iostream>
using namespace std;
int main(){
long long int tc;
cin>>tc;
for(int z=1;z<=tc;z++){
	long long int num;
	cin>>num;
	long long int temp=num,count=0;
	while(temp!=0){
		temp/=10;
		count++;
	}
	long long int arr[count],i=count;
	temp=num;
	while(temp!=0){
	arr[i-1]=temp%10;
	temp/=10;
	i--;
	}
	for(long long int j=count-1;j>0;j--){
		if(arr[j-1]>arr[j]){
			arr[j-1]--;
			for(long long int t=j;t<count;t++){
			arr[t]=9;	
			}
			
		}
	}
	cout<<"Case #"<<z<<": ";
	for(long long  int j=0;j<count;j++){
		if(arr[j]!=0)
		cout<<arr[j];
	}
	cout<<endl;
}
return 0;}