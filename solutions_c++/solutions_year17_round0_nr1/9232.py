#include <bits/stdc++.h>
using namespace std;

string changeSide(string str){
	string newS;
	for(int i=0; i<str.length(); ++i){
		if(str.at(i)=='-') newS+="+";
		else newS+="-";
	}
	return newS;
}

bool isPossible(string str){
	for(int i=0; i<str.length(); ++i){
		if(str.at(i)=='-') return false;
	}
	return true;
}

int main(){
	int T,k;
	string panc;
	cin >> T;
	int t=0;
	while(t<T){
		cin >> panc >> k;
		int size=panc.length(), cont=0;
		for(int i=0; i<size-k+1; ++i){
			char p = panc.at(i);
			if(p=='-'){
				panc=panc.substr(0,i)+changeSide(panc.substr(i,k))+panc.substr(i+k);
				cont++;
			}
		}
		string poss=panc.substr(size-k);
		bool possible=isPossible(poss);
		if(!possible) cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << t+1 << ": " << cont << endl;
		t++;
	}
	return 0;
}
