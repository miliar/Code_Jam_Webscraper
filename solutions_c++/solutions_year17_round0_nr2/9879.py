#include<iostream>
using namespace std;

 int main(){

	long long int x,y;
	long long int ans;
	cin>>x;

	for(long long int i=1;i<=x;i++){

		cin>>y;

		
		long long int check=0;
	
		while(y>0){
		long long int p=y;
		long long int prv=p%10;
			while(p>9){
			p=p/10;
			long long int first=p%10;
			if(first>prv){check=1;break;}
			prv=first;
			

			}
		if (check==0){ans=y;break;}
		y=y-1;
		
		check=0;
		}
		
		
	
		cout<<"Case #"<<i<<": "<<ans<<endl;
		



	}

}
