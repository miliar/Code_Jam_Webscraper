#include<iostream>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long int a,i,t,count,counter,prev,flag,num=1;
	cin>>t;
	while(t--){
		count=counter=flag=0;
		cin>>a;
		int arr[18];
		while(a>0){
			arr[count++]=a%10;
			a=a/10;
		}
		prev=arr[count-1];
		for(i=count-2;i>=0;i--){
			if(arr[i]>prev) counter=0;
			else if(arr[i]==prev) counter++;
			else{
				flag=2;
				if(arr[count-1]==0) { flag=1; break;}
				arr[i]=9;
				arr[i+counter+1]--;
				counter= i+counter;
				arr[counter]=9;
				break;
			}
			prev=arr[i];
		}
		if(flag==0) counter=0;
		if(arr[count-1]==0) flag=1;
		cout<<"Case #"<<num<<": ";
		if(flag==1) for(i=count-2;i>=0;i--) cout<<9;
		else {for(i=count-1;i>=counter;i--) cout<<arr[i];
		for(i=counter-1;i>=0;i--)cout<<9;}
		cout<<"\n";
		num++;
	}
}
