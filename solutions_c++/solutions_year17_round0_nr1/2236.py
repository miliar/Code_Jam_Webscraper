#include <iostream>
#include <string>

using namespace std;;

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		string cake;
		int flipper;
		cin>>cake>>flipper;
		int i;
		int n=0;
		for(i=0;i+flipper<cake.length()+1;i++){
			if(cake[i]=='-'){
				n++;
				for(int j=0;j<flipper;j++){
					if(cake[i+j]=='-') cake[i+j]='+';
					else cake[i+j]='-';
				}
			}
		}
		for(;i<cake.length();i++){
			if(cake[i]=='-') break;
		}
		if(i==cake.length()) cout<<"Case #"<<t+1<<": "<<n<<endl;
		else cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
