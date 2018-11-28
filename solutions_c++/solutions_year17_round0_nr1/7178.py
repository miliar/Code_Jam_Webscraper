

#include <iostream>
#include <string>
#include <vector>


using namespace std;

bool flip(int pos, int k, vector<bool> & s){
	if (pos + k > s.size()) return true;
	for (int i = pos; i < pos + k; i++){
		s[i] = s[i]? false : true;
	}
	return false;
}


void solve(int testnumber){
	int flipnumber = 0;
	string input;
	int k;
	cin >> input;
	cin >> k;
	vector<bool> v;
	for(char c : input){
		v.push_back(c == '+'? true : false);
	}


	bool impossible = false;

	for (int i = 0; i < v.size() && !impossible; i++){
		if (!v[i]){
			impossible = flip(i, k, v);
			flipnumber++;

		}

	
	}

	cout << "Case #" << testnumber << ": " << (impossible? "IMPOSSIBLE" : std::to_string(flipnumber)) << std::endl;;

}


int main(){
	int testcases;
	cin >> testcases;
	for (int i = 0; i < testcases; i++){
		solve(i+1);
	}
}



