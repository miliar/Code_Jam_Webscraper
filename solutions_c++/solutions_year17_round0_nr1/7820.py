// panckakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	string s;
	int T, k;
	int slen, com, m;
	int nrCase;
	ifstream in;
	in.open ("A-large.in");
	ofstream out;
	out.open("A-large.out");
	in >> T;
	for (int i = 0; i < T; i++) {
		in >> s;
		in >> k;
		slen = s.length();
		com= 0;
		for (int j = 0; j < slen;j++) {
			if (s[j] == '+')com += 1;
		}
		if (com == slen)out << "Case #" << i + 1 << ": " << "0" << endl;
		else {
			nrCase = 0;
				m = 0;
				while (s[m] == '+') {
					m++;
				}
				while (m <= (slen - k)) {		
					
				
						for (int p = m; p < (m + k); p++) {
							if (s[p] == '-')s[p] = '+';
							else s[p] = '-';
						}
						nrCase += 1;
						while (s[m] == '+') {
							m++;
						}
				}
				com = 0;
				for (int j = 0; j < slen; j++) {
					if (s[j] == '+')com += 1;
				}
				if (com == slen)out << "Case #" << i + 1 << ": " <<nrCase  << endl;
				else out << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;

		}

	}

	in.close();
	out.close();

    return 0;
}

