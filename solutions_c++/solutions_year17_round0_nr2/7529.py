#include<iostream>
#include<String.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int h=1;h<=t;++h){
	long long int n, a[20]={0}, i=-1;
	cin>>n;
	while(n){
		a[++i]=n%10;
		n/=10;
	}
	int k=i;
	while(k>0){
	if(a[k]>a[k-1]) {
		for(int m=k;m<=i;++m){
			if(a[m]==a[m+1]);
			else {k=m;break;}
		}	
		a[k]-=1; for(int j=0;j<k;++j) a[j]=9;	
		break;
	}
	k--;
}
cout<<"Case #"<<h<<": ";
for(i=19;i>=0;--i)
	if(a[i]!=0) cout<<a[i];
cout<<endl;	
}		
return 0;
}
