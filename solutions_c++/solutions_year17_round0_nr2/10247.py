#include<iostream>
using namespace std;

int main(){
long long int num,i,j;
int n,flag,dig;
cin>>n;
for(int k=0;k<n;k++){
	cin>>num;
	for(j=num;j>0;j--){
		flag=0;
		dig=num%10;
		num/=10;
		for(i=0;num>0;i++){
			if(num%10>dig){
				flag=1;
				break;
				}
			dig=num%10;
			if(num>9)
				num/=10;
			else
				num=0;
			}
		if(flag==0){
			cout<<"Case #"<<k+1<<": "<<j<<endl;
			break;
			}
		num=j-1;
		}
	}
return 0;
}