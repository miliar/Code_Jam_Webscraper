#include <iostream>
#include <string>
#include<vector>
using namespace std;


int main()
{
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, m;
		cin >> n >> m;
		vector<string> a;
		vector<bool> empty;
		int fne = -1;
		for (int i = 0; i < n; i++) {
			string s;
			cin >> s;
			a.push_back(s);
			bool e = true;
			for (int j = 0; j < s.length(); j++) {
				if (s[j] != '?') {
					e = false; break;
				}
			}
			if (!e&& fne == -1) fne = i;
			empty.push_back(e);
		}
		
		int curr = fne;
		while (curr < n) {
			if (empty[curr]) {
				a[curr] = a[curr - 1];
				curr++;
				continue;
			}
			int i = 0;
			int j = 0;
			while (i < m) {
				while (i < m& a[curr][i] == '?') i++;
				char fill = (i < m) ? a[curr][i] : a[curr][j - 1];

				for (int k = j; k < i; k++) {
					a[curr][k] = fill;
				}
				while (i < m& a[curr][i] != '?') i++;
				j = i;
			}
			if (fne != -1) {
				for (int k = 0; k < fne; k++)
					a[k] = a[curr];
				fne = -1;
			}
			curr++;
			
		}
		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < n; i++) {
			cout << a[i] << endl;
		}

	}


	
    return 0;
}

