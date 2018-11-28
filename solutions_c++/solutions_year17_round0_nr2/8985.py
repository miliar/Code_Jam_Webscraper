#include <iostream>
#include <fstream>
#include<string>
using namespace std;
int main() {
	int test=1;
	ifstream input("B-small-attempt0.in");
	ofstream output("B.txt");
	input >> test;
	for (int i = 0; i < test; i++) {
		long long int num;
		input >> num;
		bool found = false;
		while (!found) {
			string p = to_string(num);
			if (num / 10 == 0)
				found = true;
			else
				for (int w = 0; w < p.length()-1; w++) {
					if (p[w]-48 <= p[w + 1]-48) {
						found = true;
					}	
					else {
						found = false;
						break;
					}
				}
			if (!found)
				num--;
		}
		output << "Case #" << i + 1 << ": " << num<<endl;
	}
	input.close();
	output.close();
}