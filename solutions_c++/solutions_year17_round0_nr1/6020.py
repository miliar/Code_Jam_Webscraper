#include<iostream>
#include<string>
#include<vector>
using namespace std;
void flp(string &tstcase,int pos,int k){
	for(int i=pos;i<pos+k;i++){
		if(tstcase[i]=='-'){
			tstcase[i]='+';
		}
		else
			tstcase[i]='-';
	}
}
int main(){
	int t;
	cin>>t;
	for(int xx=0;xx<t;xx++){
		string tstcase;
		getline(std::cin,tstcase,' ');
		int k;
		cin>>k;
		int ctr=0,rctr=0;
		for(int i=0;i<=tstcase.size()-k;i++){
			if(tstcase[i]=='-'){
				flp(tstcase,i,k);
				ctr++;
			}
			if(tstcase.find('-')==string::npos){
				cout<<"Case #"<<xx+1<<": "<<ctr<<"\n";
				rctr=1;
				break;
			}
		}
		if(rctr==0){
			cout<<"Case #"<<xx+1<<": IMPOSSIBLE\n";
		}
	}
	return 0;
}