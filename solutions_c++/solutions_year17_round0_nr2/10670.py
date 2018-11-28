#include<iostream>
using namespace std;
int tidy(long long int n){
	long long int j,k,l,flag=0,temp;
	j=n%10;
	n=n/10;
	while(n!=0){
		flag=0;
		temp=n%10;
		if(j>=temp)
		n=n/10;
		else{
			flag=1;
			break;
		}
		j=temp;
	}
	if(flag==0)
	return 1;
	else
	return 0;
}
int main()
{
	long long int n,i,l;
	long long int j,p,k;
    cin>>n;long long int b[n];
    for(i=0;i<n;i++){
    	cin>>j;
    	for(k=j;k>=0;k--){
    		l=tidy(k);
    		if(l==1)
    		break;
		}
		b[i]=k;
	}
	for(i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": "<<b[i]<<"\n";
	}
	return 0;
}
