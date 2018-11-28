#include<iostream>
#include<string>
using namespace std;
int main(){
	int t,i,scan=0,p=0,k,len;
	long long int numb,a[10000];
	string res[100000],s;
	cin>>t;
	while(t--){
		cin>>numb;
		for(i=0;numb!=0;i++){
			a[i]=numb%10;
			numb=numb/10;
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
			if(a[i]==0 && scan==0){
				continue;
			}
			else{
				scan=1;
				s=s+ to_string(a[i]);
			}
			
			}
			res[p]=s;
			s="";
			p++;
			scan=0;
	}
	for(i=0;i<p;i++){
			cout<<"Case #"<<i+1<<": "<<res[i]<<"\n";
	}
	return 0;
}
