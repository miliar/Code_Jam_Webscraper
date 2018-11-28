#include "bits/stdc++.h"
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ct=1;ct<=t;ct++){
		string cad;
		int k;
		cin>>cad>>k;
		int cont=0;
		bool br=true;
		for (int i = 0; i < cad.length(); ++i)
		{
			if(cad[i]=='-'){
				if(i+k<=cad.length()){
					int ci=i;
					bool sw=false;
					for (int j = ci; j < ci+k; ++j)
					{
						if(cad[j]=='-'){
							cad[j]='+';
							if(!sw)i=j;
						}
						else{
							cad[j]='-';
							sw=true;
						}
					}
					//cout<<cad<<endl;
					cont++;
				}
				else{
					br=false;
					break;
				}
			}
		}
		if (!br)cout<<"Case #"<<ct<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<ct<<": "<<cont<<endl;
	}
	return 0;
}