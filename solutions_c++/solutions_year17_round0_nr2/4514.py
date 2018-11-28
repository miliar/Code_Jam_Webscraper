#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

void lastTidy(string& n, int i){
	if(i < n.size() - 1){
		lastTidy(n, i + 1);
		if(n[i] > n[i + 1]){
			n[i] = n[i] - 1;
			for(int j = i + 1;j < n.size();j++){
				n[j] = '9';
			} 
		}
	}
}


int main(){

	int T;
	string N;

	cin >> T;
	for(int i = 0;i < T;i++){
		cin >> N;
		lastTidy(N, 0);
		string res;
		int j = 0;
		while(j < N.length() && N[j] == '0'){j++;}
		for(;j < N.length();j++){
			res.push_back(N[j]);
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}

