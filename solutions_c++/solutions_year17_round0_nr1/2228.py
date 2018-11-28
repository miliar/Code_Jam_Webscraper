#include<iostream>
#include<string>
using namespace std;

string s;

inline void flip(const int k, int pos){
	for(int i=1;i<=k;i++){
		if(s[pos-i]=='+') s[pos-i]='-';
		else s[pos-i]='+';
	}
}

int minimum(const int k, int pos){
	int aux;
	if(pos == k){
		aux=1;
		if(s[0]=='+') aux = 0;
		for(int i=0;i<k;i++)
			if(s[i]!=s[0]) aux = -1;
		return aux;
	}
	else{
		if(s[pos-1]=='-'){
			flip(k,pos);
			aux = minimum(k, pos-1);
			return aux<0?-1:1+aux;
		}
		else{
			return minimum(k,pos-1);
		}
	}
}


int main(){
	int t, k, aux;
	cin >> t;
	for(int tt=1;tt<=t;tt++){
		cin >> s >> k;
		cout << "Case #" << tt << ": ";
		aux = minimum(k, s.size());
		if(aux<0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << aux << endl;
	}
	return 0;
}
