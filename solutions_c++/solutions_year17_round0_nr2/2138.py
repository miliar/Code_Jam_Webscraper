#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
ifstream in;
ofstream out;

int main(){
	in.open("input.txt");
	out.open("output.txt");
	string s;
	int T;
	in >> T;
	for (int n = 0; n < T; ++n){
		out << "Case #" << n+1 << ": ";
		in >> s;
		int a[30];
		int i;
		for (i = 0; i < s.length(); ++i){
			a[i] = s[i] - 48;
		}
		int temp = 0;
		bool b = true;
		int j = 0;
		while (j < i-1){
			if (a[j + 1] < a[j]) {
				b = false;
				break;
			}
			if (a[j + 1] > a[j]) temp = j + 1;
			++j;
		}
		if (b){
			for (int x = 0; x < i; ++x){
				out << a[x];
			}
		}
		else {
			if (a[temp] > 1){
				a[temp] = a[temp] - 1;
				for (int x = 0; x < i; ++x){
					if (x <= temp) out << a[x];
					else out << 9;
				}
			}
			else {
				for (int x = 0; x < i - 1; ++x){
					out << 9;
				}
			}

		}
		out << "\n";
	}
	in.close();
	out.close();
	return 0;
}