// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("l-out.txt");
	int t, t1 = 1;
	in >> t;
	string s;
	int k, count = 0;
	int c;

	while (t - t1 + 1) {
		count = 0;
		in >> s >> k;
		
		for (int i = 0; i <= s.size() - k; i++) {
			if (s[i] == '+') {
				//cout << s << endl;
				continue;
			}
			//cout << i << endl;
			for (int j = i; j < k + i; j++) {
				if (s[j] == '+') { s[j] = '-'; }
				else { s[j] = '+'; }
			}
			count += 1;
			//cout << s << endl;
		}
		//cout << count << endl;
		c = 0;
		for (int i = s.size() - k; i < s.size(); i++) {
			if (s[i] == '+') c += 1;
		}
		if (c == k) out << "Case #" << t1 << ": " << count << endl;
		else out << "Case #" << t1 << ": IMPOSSIBLE" << endl;

		t1 += 1;
	}

	//cin >> t;
    return 0;
}

