#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
const string valores="0123456789";

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int C,iC=1;
	string numero,resultado;
	
	bool encontrado=false;
	
	cin>>C;
	while(C--){
		cin>>numero;
		
		encontrado=false;
		string res;
		int conv=numero[0]-'0';
		int menores[numero.size()];
		for(unsigned int i=0;i<numero.size();i++){
			int val=numero[i]-'0';
			if(val<conv){
				res="";
				for(unsigned int j=i-1;j>0;j--){
					if(menores[j-1] < menores[j]){
						menores[j]=menores[j]-1;
						for(unsigned int k = 0; k < j+1; k++) res+=valores[menores[k]];
						for(unsigned int k = j+1; k < numero.size(); k++) res += '9';
						
						encontrado=true;
						resultado=res;
						break;
					}
				}
				if(encontrado==true) break;
				if(menores[0] == 1){
					for(unsigned int i=0;i<numero.size()-1;i++) res+='9';
					
					encontrado=true;
					resultado=res;
					break;
				}else{
					res += valores[menores[0]-1];
					for(unsigned int i=1;i<numero.size();i++) res += '9';
				}
				encontrado=true;
				resultado=res;
				break;
			}else if(val<=conv){
				menores[i]=conv;
			}else{
				conv=val;
				menores[i]=val;
			}
		}
		if(encontrado==false){
			for(unsigned int i=0;i<numero.size();i++)	res+='0'+menores[i];
			resultado=res;
		}
		
		cout<<"Case #"<<iC++<<": "<<resultado<<endl;
	}
	return 0;
}
