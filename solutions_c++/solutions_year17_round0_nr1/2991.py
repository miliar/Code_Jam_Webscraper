#include <iostream>

using namespace std;

int t;
string pan;
int k;
bool ok = true;
int wynik;

void zmien(int i, int z){
	for(int j=0; j<z; j++){
		pan[j+i] = ((pan[i+j]=='+')?'-':'+');
	} 
}

int main(){
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>pan>>k;
		for(int j=0; j<(int)pan.size()-k+1; j++){
			if(pan[j] == '-'){
				zmien(j,k);
				wynik++;
			}
		}
		for(int j=(int)pan.size()-k; j<(int)pan.size(); j++){
			if(pan[j] == '-'){
				ok = false;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(!ok)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<wynik<<endl;
		wynik = 0;
		ok = true;
	} 
	return 0;
}
