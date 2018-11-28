#include<bits/stdc++.h>
#include<fstream>
using namespace std;
long long minimo(long long a,long long b){
if(a<b){return a;}
return b;
}
long long maximo(long long a,long long b){
if(a>b){return a;}
return b;
}
int main(){
	ifstream fin ("entrada.in");
	ofstream fout("salida.out");
long long total;
fin>>total;
long long cont=0;
while(total!=0){
	cont++;
	total--;
	long long a,b;
	fin>>a>>b;
	vector<vector<char> >vec(a);
	for(long long i=0;i<a;i++){
		for(long long j=0;j<b;j++){
			char c;
			fin>>c;
			vec[i].push_back(c);
		}
	}
	map<char,long long>arriba;
	map<char,long long>abajo;
	map<char,long long>derecha;
	map<char,long long>izquierda;
	set<char>tam;
	vector<char>letras;
	for(long long i=0;i<a;i++){
		for(long long j=0;j<b;j++){
			if(vec[i][j]!='?'){
				arriba[vec[i][j]]=minimo(arriba[vec[i][j]],i);
				abajo[vec[i][j]]=maximo(abajo[vec[i][j]],i);
				izquierda[vec[i][j]]=minimo(izquierda[vec[i][j]],j);
				derecha[vec[i][j]]=maximo(derecha[vec[i][j]],j);
				long long tmp=tam.size();
				tam.insert(vec[i][j]);
				if(tmp!=tam.size()){
				arriba[vec[i][j]]=i;
				abajo[vec[i][j]]=i;
				derecha[vec[i][j]]=j;
				izquierda[vec[i][j]]=j;
				letras.push_back(vec[i][j]);}
			}
		}
	}
	for(long long k=0;k<letras.size();k++){
		for(long long i=arriba[letras[k]];i<=abajo[letras[k]];i++){
			for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
				vec[i][j]=letras[k];
			}
		}
	}
	for(long long k=0;k<letras.size();k++){
		long long x=1;
		long long y=1;
		long long n=1;
		long long m=1;
		for(long long i=minimo(vec[0].size()-1,derecha[letras[k]]+1);i<=minimo(vec[0].size()-1,derecha[letras[k]]+1);i++){
			for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
				if(vec[j][i]!='?'){x=0;}
			}
		}
		for(long long i=maximo(0,izquierda[letras[k]]-1);i>=maximo(0,izquierda[letras[k]]-1);i--){
			for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
				if(vec[j][i]!='?'){y=0;}
			}
		}
		for(long long i=minimo(vec.size()-1,abajo[letras[k]]+1);i<=minimo(vec.size()-1,abajo[letras[k]]+1);i++){
			for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
				if(vec[i][j]!='?'){n=0;}
			}
		}
		for(long long i=maximo(0,arriba[letras[k]]-1);i>=maximo(0,arriba[letras[k]]-1);i--){
			for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
				if(vec[i][j]!='?'){m=0;}
			}
		}
		while(x==1 or y==1 or n==1 or m==1){
			if(x==1){
                        for(long long i=minimo(vec[0].size()-1,derecha[letras[k]]+1);i<=minimo(vec[0].size()-1,derecha[letras[k]]+1);i++){
                                for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
                                        vec[j][i]=letras[k];
                                }
                        }
			derecha[letras[k]]++;
			}
			else if(y==1){
                        for(long long i=maximo(0,izquierda[letras[k]]-1);i>=maximo(0,izquierda[letras[k]]-1);i--){
                                for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
                                        vec[j][i]=letras[k];
                                }
                        }
			izquierda[letras[k]]--;
			}
			else if(n==1){
                        for(long long i=minimo(vec.size()-1,abajo[letras[k]]+1);i<=minimo(vec.size()-1,abajo[letras[k]]+1);i++){
                                for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
                                        vec[i][j]=letras[k];
                                }
                        }
			abajo[letras[k]]++;
			}
			else if(m==1){
                        for(long long i=maximo(0,arriba[letras[k]]-1);i>=maximo(0,arriba[letras[k]]-1);i--){
                                for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
                                        vec[i][j]=letras[k];
                                }
                        }
			arriba[letras[k]]--;
			}
	                for(long long i=minimo(vec[0].size()-1,derecha[letras[k]]+1);i<=minimo(vec[0].size()-1,derecha[letras[k]]+1);i++){
        	                for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
                	                if(vec[j][i]!='?'){x=0;}
	                        }
        	        }
                	for(long long i=maximo(0,izquierda[letras[k]]-1);i>=maximo(0,izquierda[letras[k]]-1);i--){
	                        for(long long j=arriba[letras[k]];j<=abajo[letras[k]];j++){
        	                        if(vec[j][i]!='?'){y=0;}
                	        }
	                }
        	        for(long long i=minimo(vec.size()-1,abajo[letras[k]]+1);i<=minimo(vec.size()-1,abajo[letras[k]]+1);i++){
                	        for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
	                                if(vec[i][j]!='?'){n=0;}
        	                }
                	}
	                for(long long i=maximo(0,arriba[letras[k]]-1);i>=maximo(0,arriba[letras[k]]-1);i--){
        	                for(long long j=izquierda[letras[k]];j<=derecha[letras[k]];j++){
                	                if(vec[i][j]!='?'){m=0;}
	                        }
        	        }
		}
	}
fout<<"Case #"<<cont<<":"<<endl;
	for(long long i=0;i<vec.size();i++){
		for(long long j=0;j<vec[i].size();j++){
			fout<<vec[i][j];
		}
		fout<<endl;
	}
}
}
