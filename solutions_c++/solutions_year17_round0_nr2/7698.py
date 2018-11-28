#include<iostream>
#include<string>
using namespace std;
int main(){
	int t,i,flag=0,p=0,k,len;
	long long int num,a[10000];
	string res[100000],s;
	cin>>t;
	while(t--){
		cin>>num;
		for(i=0;num!=0;i++){
			a[i]=num%10;
			num=num/10;
		}
		len=i;
	
		
		for(i=0;i<len-1;i++){
			if(a[i]>=a[i+1]){
			
			}
			else{
				
				a[i+1]=a[i+1]-1;
				a[i]=9;
				for(k=i-1;k>=0;k--){
					a[k]=9;
				}
			}
			
		}
		for(i=len-1;i>=0;i--){
			if(a[i]==0 && flag==0){
				continue;
			}
			else{
				flag=1;
				s=s+ to_string(a[i]);
			}
			
			}
			res[p]=s;
			s="";
			p++;
			flag=0;
	}
	for(i=0;i<p;i++){
			cout<<"Case #"<<i+1<<": "<<res[i]<<"\n";
	}
	return 0;
}
