#define _CodeJam

#ifdef _CodeJam

#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
	fstream flin, flout;
	flin.open("C:\\Users\\HamedA\\Downloads\\B-large.in", ios::in);
	flout.open("C:\\Users\\HamedA\\Downloads\\B-large.out", ios::out);
	istream& fin = flin; ostream& fout = flout;
	int t, t1;
	string s;
	int k, a;
	fin >> t;
	t1 = t;
	while (t--){
		s = "";
		fin >> s;
		for (int i = s.length(); i > 1; i--)
		{
			if (s[i - 2] > s[i - 1]){
				s[i - 2]--;
				for (int j = i-1; j < s.length(); j++)
				{
					s[j] = '9';
				}
				//fout << s << endl;
			}
		}
		if (s[0] == '0') s = s.substr(1, s.length());
		fout << "Case #" << t1 - t << ": " << s << endl;
	}
	return 0;
}

#endif