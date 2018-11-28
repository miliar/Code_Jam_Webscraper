#define _CodeJam

#ifdef _CodeJam

#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
	fstream flin, flout;
	flin.open("C:\\Users\\HamedA\\Downloads\\A-large.in", ios::in);
	flout.open("C:\\Users\\HamedA\\Downloads\\A-large.out", ios::out);
	istream& fin = flin; ostream& fout = flout;
	int t, t1;
	string s;
	int k, a;
	fin >> t;
	t1 = t;
	while (t--){
		s = "";
		fin >> s >> k;
		a = 0;
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] == '+') continue;
			if (s.length() - i < k){
				a = -1;
				break;
			}
			for (int j = 0; j < k; j++)
			{
				s[i + j] = (s[i + j] == '+') ? '-' : '+';
			}
			//fout << s << endl;
			a++;
		}
		if (a != -1)
			fout << "Case #" << t1 - t << ": " << a << endl;
		else
			fout << "Case #" << t1 - t << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}

#endif