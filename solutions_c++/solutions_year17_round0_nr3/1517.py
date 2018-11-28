#include<bits/stdc++.h>
#include<fstream>
using namespace std;
map<long long,long long>contador;
map<long long,long long>estuvo;
int main(){
ifstream fin("entrada.in");
ofstream fout("salida.out");
long long todo;
fin>>todo;
for(long long fe=0;fe<todo;fe++){
	fout<<"Case #"<<fe+1<<": ";
	long long a,b;
	fin>>a>>b;
	long long rsp1,rsp2;
	long long x=0;
	vector<pair<long long,long long> >vec;
	pair<long long,long long>par;
	par.first=a;
	par.second=1;
	vec.push_back(par);
	long long g=0;
	while(x<b and g==0){
		vector<pair<long long,long long> >nuevo;
		for(long long i=0;i<vec.size();i++){
			if(vec[i].first!=0 and g==0){
				if(x+vec[i].second>=b){
					g=1;
					vec[i].first--;
					if(vec[i].first%2==0){rsp1=vec[i].first/2;rsp2=vec[i].first/2;}
					else{
						rsp1=(vec[i].first/2)+1;
						rsp2=(vec[i].first/2);
					}
				}
				else{x=x+vec[i].second;}
				if(g==0){
				vec[i].first--;
				if(vec[i].first%2==0){
					long long y=0;
					long long r=0;
					for(long long j=0;j<nuevo.size();j++){
						if(nuevo[j].first==(vec[i].first)/2){
							y=1;
							r=j;
						}
					}
					if(y==1){
						nuevo[r].second=nuevo[r].second+2*vec[i].second;
					}
					else{
						pair<long long,long long>tu;
						tu.first=vec[i].first/2;
						tu.second=2*vec[i].second;
						nuevo.push_back(tu);
					}
				}
				else{
					long long y1=0;
					long long r1=0;
					for(long long j=0;j<nuevo.size();j++){
						if(nuevo[j].first==(vec[i].first/2)+1){
							y1=1;
							r1=j;
						}
					}
					if(y1==1){
						nuevo[r1].second=nuevo[r1].second+vec[i].second;
					}
					else{
						pair<long long,long long>tu;
						tu.first=((vec[i].first)/2)+1;
						tu.second=vec[i].second;
						nuevo.push_back(tu);
					}
					long long y2=0;
					long long r2=0;
					for(long long j=0;j<nuevo.size();j++){
						if(nuevo[j].first==(vec[i].first/2)){
							y2=1;
							r2=j;
						}
					}
					if(y2==1){
						nuevo[r2].second=nuevo[r2].second+vec[i].second;
					}
					else{
						pair<long long,long long>tu;
						tu.first=(vec[i].first/2);
						tu.second=vec[i].second;
						nuevo.push_back(tu);
					}
				}
				}
			}
		}
		if(g==0){
			sort(nuevo.begin(),nuevo.end());
			for(long long i=0;i<nuevo.size()/2;i++){
				pair<long long,long long> tmp=nuevo[nuevo.size()-i-1];
				nuevo[nuevo.size()-i-1]=nuevo[i];
				nuevo[i]=tmp;
			}
			vec=nuevo;
		}
	}
	fout<<rsp1<<" "<<rsp2<<endl;
}
}
