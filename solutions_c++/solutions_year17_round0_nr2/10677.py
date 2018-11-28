// B1.cpp: Okreœla punkt wejœcia dla aplikacji konsoli.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

bool cons(string s);
string mix(string s);
int main()
{
	ifstream in("small.in");
	ifstream out("small.txt");
	fstream file;
	string s;
	int counter = 1;
	
	while (in >> s)
	{


		if (cons(s) == true)
		{
			file.open("small.out", ios::out | ios::app);
			file << "Case #" << counter << ": " << mix(s) << endl;
			file.close();
			cout << "case #" << counter << ": " << mix(s);

		}
		else if (cons(s) == false) {
			file.open("small.out", ios::out | ios::app);
			file << "Case #" << counter << ": " << s << endl;
			file.close();
			cout << "case #" << counter << ": " << s;

		}
		counter++;
	}
	
	
    return 0;
}
bool cons(string s)
{
	int a = s.length();
	
	if (a == 1) return false;
	for (int x = 0; x <a-1; x++) {
		
		if (s[x] > s[x + 1]) {
			cout << s[x] << "	" << s[x + 1] << endl;
			return true;
			break;
		}
			
		}
	return false;
	
}
string mix(string s)
{int a = atoi(s.c_str());
string s2;
	do {
		a--;
		s2 = to_string(a);
		
		
	} while (cons(s2) == true);

	return s2;
}
