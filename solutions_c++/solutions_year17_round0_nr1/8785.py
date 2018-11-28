#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
	int num = 0;
	int count = 0;
	string s;
	string test;
	int t = 0;
	int k = 0;
	string outp;
	/*
		string myStream = "45";
	istringstream buffer(test);
	ifstream ifs;
	ifs.open("A-small-attempt0.txt");
	test = ifs.getline();
	int value;
	buffer >> value;
	*/
	cin >> num;

	string v[num];
	for (int c = 0; c < num; c++) {
		cin >> s;
		cin >> k;
		for (int a = 0; a < s.length(); a++) {
			if (a + k > s.length()) {
				break;
			}
			if (s.substr(a, 1).compare("-") == 0) {
				s.replace(a,1,"+");
				count++;
				for (int b = 1; b < k; b++) {
					
					if (s.substr(a+b,1).compare("-") == 0) {
						s.replace(a+b,1,"+");
					}
					else {
						s.replace(a+b,1,"-");
					}
				}

			}
		}
		for (int d = 0; d < s.length(); d++) {
			if (s.substr(d,1).compare("-") == 0) {
			
				v[c]= "IMPOSSIBLE";
				break;
			}
			if (d == s.length() - 1) {
				
		

				ostringstream convert;   // stream used for the conversion

				convert << count;
				v[c] = convert.str();
			}
		}
		//cout << "Case #" << c+ 1 << ": " << outp << endl;
		count = 0;
		
	}
	
	for (int f = 0; f < num; f++) {
		cout << "Case #" << f+1 << ": " << v[f] << endl;
	}
	
	return 0;
}