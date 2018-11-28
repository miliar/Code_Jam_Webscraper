#include <iostream>
#include <string.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int z=1;z<=t;z++){
		char a[1010];
		cin>>a;
		int f;
		cin>>f;
		int count=0;
		for(int i=0;i<=strlen(a)-f;i++){
			if(a[i]=='-'){
				count++;
				for(int j=0;j<f;j++){
					if(a[i+j]=='-') a[i+j]='+';
					else	a[i+j]='-';
				}
			}
		}
		int fl=1;
		for(int i=0;i<strlen(a);i++){
			if(a[i]=='-'){
				cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
				fl=0;
				break;
			}
		}
		if(fl){
			cout<<"Case #"<<z<<": "<<count<<endl;
		}
	}
}