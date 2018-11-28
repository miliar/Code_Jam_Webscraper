#include<iostream>
#include<string>
#include<stdio.h>
#include<ctype.h>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string sc = {};
		bool hantei[1001] = {};
		int cou = 0;
		int k = 0;
		int kotae = 0;
		cin >> sc >> k;
		while (sc[cou]) {
			if (sc[cou] == '+') {
				hantei[cou] = true;
			}
			cou++;
		}
		for (int o = 0; o < cou - k + 1; o++)
		{
			if (hantei[o] == false) {
				for (int xxx = o; xxx < o + k; xxx++)
				{
					if (hantei[xxx] == false) { hantei[xxx] = true; }
					else { hantei[xxx] = false; }
				}
				kotae++;
			}
		}
		bool dgt = true;
		for (int dgf = cou - k; dgf < cou; dgf++)
		{
			//cout << k << "aa";
			//cout << hantei[dgf];
			if (hantei[dgf] == false) {
				cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl; dgt = false; break;
			}
		}
		if (dgt == true) { cout << "Case #" << i + 1 << ": " << kotae << endl; }
	}
	return 0;
}

