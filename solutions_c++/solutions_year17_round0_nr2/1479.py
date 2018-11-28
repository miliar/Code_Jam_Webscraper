#include<bits/stdc++.h>
using namespace std;
long long convertir(char t){
	long long r=t-48;
	return r;
}
int main(){
	ifstream fin("entrada.in");
	ofstream fout("salida.out");
	long long n;
	fin>>n;
	for(long long u=0;u<n;u++){
		fout<<"Case #"<<u+1<<": ";
		string p;
		fin>>p;
		vector<long long>vec;
		for(long long i=0;i<p.size();i++){
			vec.push_back(convertir(p[i]));
		}
		vector<long long>rsp;
		rsp.push_back(vec[0]);
		for(long long i=1;i<vec.size();i++){
			if(vec[i]<vec[i-1]){
				for(long long j=i;j<vec.size();j++){
					rsp.push_back(9);
				}
				rsp[i-1]--;
				break;
			}
			else {rsp.push_back(vec[i]);}
		}
		for(long long i=rsp.size()-1;i>=1;i--){
			if(rsp[i-1]>rsp[i]){
				rsp[i]=9;
				rsp[i-1]--;
			}
		}
		for(long long i=0;i<rsp.size();i++){
			if(i==0 and rsp[i]==0){
			}
			else{fout<<rsp[i];}
		}
		fout<<endl;
	}
}
