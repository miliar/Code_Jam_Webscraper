#include<iostream>
using namespace std;
long long input, pow[25];
int ln;
int findln(){
	int res=0;
	long long tmp=1;
	while(input/tmp>0)tmp*=10, res++;
	return res;
}
void setpow(){
	long long temp=1;
	for(int x=0;x<20;x++){
		pow[x]=temp;
		temp*=10;
	}
}
int solnum(int index){
	return (input/pow[ln-1-index])%10;
}
void dec(int index){
//	cout<<solnum(index)<<" "<<solnum(index-1)<<endl;
	while(index>0 && solnum(index)<solnum(index-1)){
		if(solnum(index)==0)input-=pow[ln-index-1];
		else input-=(solnum(index-1)-solnum(index))*pow[ln-index];
		input+=(9-solnum(index))*pow[ln-index-1];
//		cout<<"alter "<<index-1<<" by "<<solnum(index-1)-solnum(index)<<endl;
//		cout<<input<<endl;
		index--;
	}
}
int main(){
	setpow();
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>input;
		ln=findln();
		for(int x=0;x<ln;x++){
			if(solnum(x)<solnum(x-1)){
//				cout<<"found untidy "<<x<<" at value "<<solnum(x)<<endl;
//				cout<<"-%"<<pow[ln-x]<<"-1"<<endl;
				input-=input%pow[ln-x];
				
				input--;
//				cout<<input<<endl;
				dec(x-1);
				break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<input<<endl;
	}
	return 0;
}
