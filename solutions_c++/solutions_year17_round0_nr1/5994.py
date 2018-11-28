#include <iostream>
#include <string>
#include <fstream>>

using namespace std;

int n;
string str[101];
int k[101];


int out[101];

void input() {
	ifstream fin("input.txt");
	fin >> n;

	for (int i = 0; i < n; i++) 
	{
		fin >> str[i] >> k[i];
	}

}

int check(string r) {

	int ch = 0;
	for (int i = 0; i < r.length(); i++) {
		char tmp = r.at(i);
		if (tmp == '+') ch++;
	}

	if (ch == r.length()) {
		return 1;
	}
	else return 0;

}

void proc(int in) {
	string res = str[in];
	int cnt = k[in];
	int resCnt = 0;
	int ch = 0;
	for (int i = 0; i < res.length(); i++) {
		char tmp = res.at(i);
		if (tmp == '+') ch++;
	}

	if (ch == res.length()) {
		out[in] = 0;
		return;
	}

	
	while (1) {
		int ccc;
		int s = res.find("-");

		ccc = 0;
		for (int j = 0; j < cnt; j++) {
			if (s + cnt <= res.length()) {
				if (res.at(s + j) == '+') {
					res.replace(s + j, 1, "-");
				}
				else res.replace(s + j, 1, "+");
			}
			else {

			}
		}
		if (resCnt > 1000) ccc = 1;

		resCnt++;

		if (check(res) == 1) {
			out[in] = resCnt;
			return;
		}
		else {
			if (ccc == 1) {
				out[in] = -1;
				return;
			}
		}


	}


}

void output() {
	ofstream fout("output.txt");
	for (int i = 1; i <= n; i++) {
		fout << "Case #";
		fout << i;
		fout << ": ";
		if (out[i-1] == -1) {
			fout << "IMPOSSIBLE" << endl;
		}
		else fout << out[i-1] << endl;
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