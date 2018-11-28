#include<iostream>
#include<cstdio>
using namespace std;

int volteos(string pan,int k){
	int n=pan.size();
	int cant=0;
	for(int i=0;i<n-k+1;i++){
		if (pan[i]=='-'){
			cant++;
			for(int j=0;j<k;j++){
				if(pan[i+j]=='-') pan[i+j]='+';
				else pan[i+j]='-';
			}
		}
	}
	for(int i=0;i<n;i++){
		if (pan[i] == '-') return -1;
	}
return cant;
}

int main(){
	//freopen("testa.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int C,iC=1,k,cant=0;
	string pan;
	cin>>C;
	while(C--){
		cin>>pan>>k;
		cant=volteos(pan,k);
		if(cant==-1)
			cout<<"Case #"<<iC++<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<iC++<<": "<<cant<<endl;
	}
	return 0;
}
