#include <iostream>
#include <string>

using namespace std;

int check(string n){
	for(unsigned i = 0; i < n.length() - 1; i++){
		if(n[i] > n[i+1]){
			return i;
		}
	}
	return -1;
}

string prev(string n){
	int pos = check(n);
	if(pos == -1){
		return n;
	}
	else{
		n[pos]--;
		for(unsigned i = pos+1; i < n.length(); i++)
			n[i] = '9';
		return prev(n);
	}
}

int main(){
	int T;
	string N;
	cin >> T;

	for(int i = 1; i <= T; i++){
		cin >> N;
		string last;

		last = prev(N);

		unsigned j = 0;
		while(last[j] == '0' && j < last.length())
			last.erase(last.begin() + j);

		cout << "Case #" << i << ": " << last << endl;
	}
}