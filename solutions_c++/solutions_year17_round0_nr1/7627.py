#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		string input;
		cin>>input;
		int k, count=0,check=0;
		cin>>k;
		int len = input.length();
//		cout<<len<<" "<<k<<"\n";
		for(int j=0;j<len;j++){
			if(input[j]=='-'){
				count++;
//				cout<<"i: "<<j<<"\n";
				for(int z=0;z<k;z++){
					if((j+k)<=len){
						if(input[j+z]=='-')
							input[j+z]='+';
						else
							input[j+z]='-';
					}
				}
			}

//			cout<<input<<"\n";
		}

		for(int j=0;j<len;j++){
			if(input[j]=='-'){
				check=1;
				break;
			}
		}

		cout<<"Case #"<<(i+1)<<": ";
		if(check==1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<count<<"\n";
		


	}
}