#include <iostream>
#include <string.h>
using namespace std;

string prev_tidy(string N);

int main(){
	int T;
	string N;
	
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> N;
		string tidystr = prev_tidy(N);
		cout << "Case #" << i+1 << ": " << tidystr << endl;
	}
}

string prev_tidy(string N){
	//index=0
	//mirar el siguiente
	//si es mayor i++ y index=i
	//si es igual i++
	//si es menor tonines desde index
	string tidy = N;
	int l = N.length();
	int act, index;
	bool tonines = false;
	index = 0;
	
	for(int i=0;i<l;i++){
		act = tidy[i] - '0';
		int j = i+1;
		if(j<l){
			if(tidy[j]-'0'>act){
				index = i + 1;
			}
			else if(tidy[j]-'0'<act){
				tonines = true;
				break;
			}
		}
		if(tonines) break;
	}
	if(tonines){
		tidy[index] = tidy[index] - 1;
		for(int i=index+1;i<l;i++){
			tidy[i] = '9';
		}
	}
	if(tidy[0]=='0') tidy = tidy.substr(1, l-1);
	
	return tidy;
}

