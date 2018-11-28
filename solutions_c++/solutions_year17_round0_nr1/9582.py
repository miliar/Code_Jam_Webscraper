#include <iostream>
#include <cstdio>

using namespace std;

bool verify(string cad){
	for(int i=0;i<cad.length();i++){
		if(cad[i]=='-')return false;
	}
	return true;
}

int main(){
	int T,K;
	cin>>T;
	for(int cases=0;cases<T;cases++){
		string cad;
		cin>>cad>>K;
		int ncad=cad.length();
		int ans=0;
		for(int i=0;i<ncad-K+1;i++){
			if(cad[i]=='-'){
				ans++;
				for(int j=i;j<i+K;j++){
					if(cad[j]=='-')cad[j]='+';
					else cad[j]='-';
				}
			}
		}
		if(verify(cad)){
			cout<<"Case #"<<cases+1<<": "<<ans<<endl;
		}else{
			cout<<"Case #"<<cases+1<<": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}