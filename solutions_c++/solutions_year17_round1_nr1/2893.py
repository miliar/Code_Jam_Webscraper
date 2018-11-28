// google_code_jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	int r, c;
	cin >> t;  
	for (int x = 1; x <= t; ++x) {
		cin >> r >> c;

		char* arr = new char[r*c];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> arr[i*c + j];
			}
		}
		
		/*for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << arr[i*c + j] << "\t";
			}
			cout << endl;
		}
		cout << endl;*/

		int met[1000];
		memset(met, 0, sizeof met);


		// go right
		int i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?' && met[0+arr[i]] == 0) {
				int j = i + 1;
				char initial = arr[i];
				while (j < cr*c + c && arr[j] == '?') {
					arr[j] = initial;
					i++;
					j++;
					met[0 + initial] = 2;
				}
			}

			i++;
		}

		// go left
		i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?' && (met[0 + arr[i]] == 0 || met[0 + arr[i]] == 2)) {
				int j = i - 1;
				char initial = arr[i];
				while (cr*c <= j && arr[j] == '?') {
					arr[j] = initial;
					j--;
					met[0 + initial] = 2;
				}
			}

			i++;
		}

		// go bottom
		i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?' && (met[0 + arr[i]] == 0)) {
				int j = i + c;
				char initial = arr[i];
				while (j < r*c  && arr[j] == '?') {
					arr[j] = initial;
					j+=c;
					met[0 + initial] = 1;
				}
			}

			i++;
		}

		// go bottom
		i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?' && (met[0 + arr[i]] == 0 || met[0 + arr[i]] == 1)) {
				int j = i - c;
				char initial = arr[i];
				while (j >= 0  && arr[j] == '?') {
					arr[j] = initial;
					j -= c;
					met[0 + initial] = 1;
				}
			}

			i++;
		}

		// handle empty rows
		/*i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?') {
				char initial = arr[i];
				int dj = i - 1;
				while (dj >= 0 && arr[dj] == '?') {
					arr[dj] = initial;
					dj--;
				}
				int uj = i + c;
				while (uj < r*c && arr[uj] == '?') {
					arr[uj] = initial;
					uj++;
				}
				if (uj > i + c) {
					continue;
				}
			}

			i++;
		}*/
		
		i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?') {
				int j = i + c;
				char initial = arr[i];
				while (j < r*c  && arr[j] == '?') {
					arr[j] = initial;
					j += c;
					met[0 + initial] = 1;
				}
			}

			i++;
		}

		// go bottom
		i = 0;
		while (i < r*c) {
			int cr = i / c;
			int cc = i % c;

			if (arr[i] != '?') {
				int j = i - c;
				char initial = arr[i];
				while (j >= 0 && arr[j] == '?') {
					arr[j] = initial;
					j -= c;
					met[0 + initial] = 1;
				}
			}

			i++;
		}
		
		cout << "Case #" << x << ":" << endl;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << arr[i*c + j];
			}
			cout << endl;
		}
	}

	return 0;
}

