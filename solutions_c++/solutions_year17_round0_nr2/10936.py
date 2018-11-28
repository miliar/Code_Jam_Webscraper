#include<iostream>
#include<fstream>
using namespace std;
long myfunc(int);


long myfunc(int N){
	
	long temp,c=0;
	temp = N;
	while(temp!=0){
		temp = temp/10;
		c++;
	}
	temp = N;
	long arr[c],k,z;
	
	for(k=0;k<c;k++){
		arr[k]=temp%10;
		temp=temp/10;
	}
	for(z=0;z<c-1;z++){
		if(arr[z]<arr[z+1])
		break;
	}
	if(z==c-1)
	return N;
	
	else return myfunc(N-1);
}
int main(){
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output1.out","w",stdout);
	long T,N,i,j;
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>N;
		if(N/10 == 0)
		cout<<"Case #"<<i<<":"<<" "<<N<<"\n";
		
		else{
			cout<<"Case #"<<i<<":"<<" "<<myfunc(N)<<"\n";
		}
	}
	
	
	return 0;
}
