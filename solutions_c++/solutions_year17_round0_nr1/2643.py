#include<fstream>
#include<iostream>
#include <cstring>
#include <string>

using namespace std;


void flip(char *p) {
	if ((*p) == '-') (*p) = '+';	
	else (*p) = '-';
	
}

void flip_k(char * bgn, int k) {
	for (char * it = bgn; it != bgn + k; ++ it)  flip(it);
}

int make_happy(char * s, int n, int k) {
	cout << endl;
	char * bgn = s;
	char * lim = s + (n - k);
	int flipcounter = 0;
	while (bgn != lim) {
		if ((*bgn) == '-') {
			//cout << "Before:" <<  string(s) << " ";
			flip_k(bgn, k);
			++ flipcounter;
			//cout << "After:" << string(s) << endl;
		}
		++ bgn;
	}
	for (char * it = lim; it != s + n; ++ it)  {
		if ((*it) == '-') {
			//cout << "Before:" <<  string(s) << " ";
			flip_k(lim, k);
			++ flipcounter;
			//cout << "After:" << string(s) << endl;
			break;
		}
	}
	for (char * it = s; it != s + n; ++ it)  {
		if ((*it) == '-') return (-1);
	}
	return flipcounter;
	
}

int main()
{
	int t;
	
	ifstream inputfile("a.in");
	ofstream outputfile("a.out");
	
	inputfile >> t;	
	
	for (int i = 0; i < t; ++ i)
	{
		string str;
		int k = 0;
		inputfile >> str >> k;
		int n = str.length();		
		char * cstr = new char [n + 1];
  		strcpy (cstr, str.c_str());
  		
		int res = make_happy(cstr, n, k);
		//cout << str << " " << res << endl;
		
		outputfile << "Case #" << i + 1 << ": ";
		if (res == -1) outputfile << "IMPOSSIBLE" << endl;
		else outputfile << res << endl;
	}
}
