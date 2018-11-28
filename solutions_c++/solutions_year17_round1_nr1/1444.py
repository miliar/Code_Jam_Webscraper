#include <bits/stdc++.h>
using namespace std;

void cake() {
	int n, m;
	cin >> n >> m;
	string vet[n];
	for (int i = 0; i < n; i++) {
		cin >> vet[i];
	}
	vector<string *> empty;
	char first[n];
	string lastfull = "";
	for (int i = 0; i < n; i++) {
		first[i] = '?';
		bool flag = false;
		for (int j = 0; j < m; j++) {
			if (vet[i][j] != '?') {
				if (first[i] == '?') {
					first[i] = vet[i][j];
				}
				flag = true;
			}
		}
		if (!flag) {
			if (lastfull == "")
				empty.push_back(&vet[i]);
			else {
				vet[i] = lastfull;
			}
		}
		else {
			for (int j = 0; j < m; j++) {
				if (vet[i][j] == '?') {
					vet[i][j] = first[i];
				}
				else {
					first[i] = vet[i][j];
				}
			}
			lastfull = vet[i];
			while (!empty.empty()) {
				*(empty.back()) = lastfull;
				empty.pop_back();
			}
		}
	}
	for (int i = 0; i < n; i++) {
		cout << vet[i] << endl;
	}
	
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cout << "Case #" << i + 1 << ":" << endl;
		cake();
	}
}
