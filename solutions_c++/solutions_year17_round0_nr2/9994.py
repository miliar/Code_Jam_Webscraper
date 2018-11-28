#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int c = 1; c <= t; c++) {
		// Entrada
		string s; cin >> s;
		vector<int> v(s.size());
		for (int i = 0; i < s.size(); i++){
			v[i] = ((int)s[i] - (int)'0');
		}

		// Algo
		for (int i = 0; i < v.size()-1; i++) {
			if (v[i+1] < v[i]) {
				//Meto reversa
				int j = i;
				while (j >= 1 && v[j-1] == v[i]) j--;
				v[j]--;
				j++;
				while (j < v.size()) {
					v[j] = 9;
					j++;
				}
			}
		}

		// Salida
		cout << "Case #" << c << ": ";
		bool started = false;
		for (int i = 0; i < v.size(); i++) {
			if (v[i] != 0) started = true;
			if (started) cout << v[i];
		}
		cout << endl;
	}
}