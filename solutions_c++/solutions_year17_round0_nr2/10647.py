#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,n;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		int x=n;
		while(x>=1){
			int temp=x,flag=0;
			while(temp!=0){
				int u=temp%10;
				temp=temp/10;
				if(u<temp%10){
					flag=1;break;
				}
			}
			if(flag==1){
				x--;
			}
			else{
				cout<<"Case #"<<i+1<<": "<<x<<endl;
				break;
			}
		}
	}
	return 0;
}
