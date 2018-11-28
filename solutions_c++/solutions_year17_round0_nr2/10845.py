#include <iostream>
using namespace std;

int main(){

	int t;cin>>t;
	int j;
	unsigned long long int n,m,i;
	bool isTidy;
	int first,second;

	for(j=1;j<=t;j++){

		cin>>n;
		
		for(i=n;i>=1;i--){

			m=i;

			isTidy=true;

			first=m%10;

			while(m!=0){

				m/=10;

				second=m%10;

				if(second>first){
					isTidy=false;
					break;
				}

				first=second;

			}

			if(isTidy){
				cout<<"Case #"<<j<<": "<<i<<endl;
				break;
			}

		}

	}	
	

	return 0;

}