#include<bits/stdc++.h>
using namespace std;

bool trueTidy(string &data){
	bool res = true;
	int aux = 0;
	
	if(data.size() == 0){
		(data[0] == '0')?res = false:res;
	}
	
	for(int x = 0; x < data.size(); x++){
		if(aux > data[x]-'0')
			return false;
		aux = data[x]-'0';
	}
	return res;
}

void res(string &data){
	int aux, size = data.size(),flag=1;
	
	/*if(data[data.size()-1] == '0'){
		string aux_data = "";
		for(int x = 0; x < data.size()-1; x++){
			aux_data += '9';
		}
		data = aux_data;
		return;
	}*/
	
	while(size && flag){
		aux = (data[size-1]-'0' - 1);
		if(aux < 0){
			data[size-1] = '9';
			size --;
		} else{
			data[size-1] = aux + '0';
			flag = 0;
		}
	}

	if(data[0] == '0'){
		string aux_data = "";
		for(int x = 1; x < data.size(); x++){
			aux_data += data[x];
		}
		data = aux_data;
	}
}

int main(){
	int numberCases,contCase=1;
	string data;
	cin>> numberCases;
	while(numberCases --){
		cin>>data;
		while(!trueTidy(data)){
			res(data);
		}
		cout<<"Case #"<<contCase<<": "<<data<<'\n';
		contCase++;
	}

}