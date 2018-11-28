#include<iostream>
using namespace std;
int main(){
	int t;
	int n;
	int j=1;
	int i=0;
	cin>>t;
	while (i!=t){
		cin>>n;
		if (n<10){cout<<"Case #"<<j<<": "<<n<<endl; j++;
		}
		else{
			while(n>8){
				if (((n%10) >= (n/10)%10 and (n/10)%10 >= (n/100)%10 and (n/100)%10 >= (n/1000)%10)){
				cout<<"Case #"<<j<<": "<<n<<endl;
				j++;
				break;
			}
			n-=1;
			}
			}
		i++;
		}
	return 0;	
	}
