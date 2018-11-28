#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	int k=1;
	while(t--){
	long long n;
	cin>>n;
	long long s1=-1,s2;
	long long nm=10,nm2;
	bool b=true;
	long long j=n;
	
	if(n<=9)
	s1=n;
	
	else {
	for(long long i=n;i>=9;i--){
		j=i;
		nm=10;
		b=true;
	
		while((j/10!=0)&&b)
		{
			nm2=j%10;
		  
		if(nm2<=nm)
		{
			nm=nm2;
			 j/=10;
		}
		
		else
		b=false;
	
	
		}
		

		if(j/10==0&&j<=nm){
		s1=i;
		break;
	}
	

	}
	}
	
	printf("Case #%d: %lld\n",k,s1);
	
	k++;
	}
	
	// your code goes here
	return 0;
}