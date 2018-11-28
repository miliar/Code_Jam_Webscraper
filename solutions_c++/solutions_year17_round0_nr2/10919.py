#include <iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	int a=1;
	while(t--){
		 long long int n;
		cin>>n;
		long long int check=n;
		while(check>0){
			long long int m=check%10;
			long long int z=check/10;
			long long int p=z%10;
			if(p<=m){
				check=check/10;
			}else{
				n--;
				check=n;
			}
		}
		cout<<"case #"<<a<<": "<<n<<endl;
		a++;
	}
} 
