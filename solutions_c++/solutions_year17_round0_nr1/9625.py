#include <iostream>
using namespace std;

char flipPancake(char input){
	if(input=='+'){
		return '-';
	}else if(input=='-'){
		return '+';
	}
}

int main() {

	int n;
	cin>>n;
	string data;
	int k;
	string res="";
	for(int i=0;i<n;i++){
		cin>>data;
		cin>>k;
		int counter=0;
		bool possible = true;
		int tamano = data.size();
		for(int j=0;j<tamano;j++){
			if(data[j]=='-'){
				if(j+k<=tamano){
					for(int m=0;m<k;m++){
						data[j+m] = flipPancake(data[j+m]);
					}
					counter++;
				}else{
					possible=false;
				}
			}
		}
		if(possible){
			cout<< "Case #"<<i+1<<": "<<counter<<endl;
		}else{
			cout<< "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		counter=0;
		possible=true;

	}
	return 0;
}
