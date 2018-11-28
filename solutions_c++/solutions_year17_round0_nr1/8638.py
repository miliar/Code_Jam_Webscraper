#include <bits/stdc++.h>
using namespace std;

int main () {
	
	int t=0, k=0, i=0, num=0, j=0; 
	string s="";

	int panque[1000];

	cin >> t;

	for (int c=1; c<=t; c++) {

		cin >> s >> k;

		int tam = s.length();

		//cout << s << endl;

		num = 0;
		for (i=0; i<tam; i++) {
			if (s[i] == '+') { panque[i] = 1; num++; }
			else panque[i] = 0;

		}

		//for (int idx=0; idx<tam; idx++) cout << panque[idx] << " ";
		//cout << endl;

		if (num == tam) cout << "Case " << (char)(35) << c << (char)(58) << " " << "0" << endl;
		else {

			num = 0;
			for (i=0; i<=tam-k; i++) {

				if (panque[i] == 0) {
					num++;
					for (j=i; j<k+i; j++) {
						if (panque[j] == 0) panque[j] = 1;
						else panque[j] = 0;
					}
				}

				//for (int idx=0; idx<tam; idx++) cout << panque[idx] << " ";
				//cout << endl;

			}

			for (i=0; i<tam; i++) 
				if (panque[i] == 0) break;
			
			if (i == tam) cout << "Case " << (char)(35) << c << (char)(58) << " " << num << endl;
			else cout << "Case " << (char)(35) << c << (char)(58) << " " << "IMPOSSIBLE" << endl;

		}

	}

	return 0;
}