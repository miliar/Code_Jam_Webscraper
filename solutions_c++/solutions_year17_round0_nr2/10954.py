#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

bool is_tidy(string s)
{
	
	for (int i = 1;i < s.length(); i++) {
		if (s[i - 1] > s[i])
			return 0;
	}
	return 1;
}

int nondec (string s)							//индекс конца неубывающей последовательности
{
	for (int i = 1;i < s.length(); i++) {
		if (s[i - 1] > s[i])
			return i-1;
	}
	return -1;
}

void atos(long long n, string& s)
{
	s = "";
	while (n)
	{
		switch (n%10)
		{
		case(0): {s.push_back('0'); n /= 10;break;}
		case(1): {s.push_back('1'); n /= 10;break;}
		case(2): {s.push_back('2'); n /= 10;break;}
		case(3): {s.push_back('3'); n /= 10;break;}
		case(4): {s.push_back('4'); n /= 10;break;}
		case(5): {s.push_back('5'); n /= 10;break;}
		case(6): {s.push_back('6'); n /= 10;break;}
		case(7): {s.push_back('7'); n /= 10;break;}
		case(8): {s.push_back('8'); n /= 10;break;}
		case(9): {s.push_back('9'); n /= 10;break;}
		}
	
	}
	reverse(s.begin(), s.end());
}

long long find_tidy(long long d,string s)
{
	atos(d,s);
	int a = nondec(s);
	while (!is_tidy(s)) {
		if (a == -1)
			return _atoi64(s.c_str());
		if (s[a] > '0')	{
			s[a] = (char)(s[a] - 1);
			for (int i = a + 1; i < s.length(); i++) {
				if (s[i] == '9')
					break;
				s[i] = '9';
			}
			a = nondec(s);
		}
		else { 
			a--;
		}
	}
	return _atoi64(s.c_str());
}

int main()
{
	ifstream fin;
	ofstream fout;
	int t;
	string n;
	fin.open("B-small-attempt1.in");
	fout.open("test.out");
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n;
		if (is_tidy(n))
			fout << "Case #" << i+1 << ": " << n << endl;
		else {
			fout << "Case #" << i + 1 << ": " << find_tidy(_atoi64(n.c_str()), n) << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}