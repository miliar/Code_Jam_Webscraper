#include <iostream>
#include <string>
#include <fstream>>

using namespace std;

int n;
string str[101];
string out[101];

void input() {
	ifstream fin("input.txt");
	fin >> n;

	for (int i = 0; i < n; i++) 
	{
		fin >> str[i];
	}

}

int check(string str) {

	for (int i = 0; i < str.length()-1; i++) {
		if (str.at(i) <= str.at(i + 1)) {
			
		}
		else return 0;
	}

	return 1;
}
string minus1(string str) {
	string r = str;
	int flag;


	int aa = 1;
	flag = 0;

	for (int j = str.length()-1; j > 0; j--) {
		if (str.at(j) == '9') aa++;
		else break;
	}

	for (int i = str.length() - aa; i >= 0; i--) {

		char a = r.at(i);

		if (a == '9') {
			r.replace(i, 1, "8");
			break;
		}
		else if (a == '8') {
			r.replace(i, 1, "7");
			break;
		}
		else if (a == '7') {
			r.replace(i, 1, "6");
			break;
		}
		else if (a == '6') {
			r.replace(i, 1, "5");
			break;
		}
		else if (a == '5') {
			r.replace(i, 1, "4");
			break;
		}
		else if (a == '4') {
			r.replace(i, 1, "3");
			break;
		}
		else if (a == '3') {
			r.replace(i, 1, "2");
			break;
		}
		else if (a == '2') {
			r.replace(i, 1, "1");
			break;
		}
		else if (a == '1') {
			r.replace(i, 1, "0");
			break;
		}
		else if (a == '0') {
			if (i > 0) {
				r.replace(i, 1, "9");
				flag = 1;
			}
		}
	}

	if (r.at(0) == '0') {
		r.erase(0, 1);
	}

	return r;
}
void proc(int in) {
	string res = str[in];

	while (1) {
		
		if (check(res) == 1) {
			out[in] = res;
			return;
		}

		res = minus1(res);
	}
}

void output() {
	ofstream fout("output.txt");
	for (int i = 1; i <= n; i++) {
		fout << "Case #";
		fout << i;
		fout << ": ";
		fout << out[i-1] << endl;
	}
}
void main()
{
	input();

	for (int i = 0; i < n; i++) {
		proc(i);
	}

	output();
}