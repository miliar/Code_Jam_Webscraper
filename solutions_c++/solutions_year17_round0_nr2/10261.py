#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool isnumberincreasing(unsigned long long n);
unsigned long long numberofnumbers(string n);

int main()
{
	ifstream myIn;
	myIn.open("C:\\Users\\Simeon\\Downloads\\B-small-attempt5.in");
	ofstream MyOut;
	MyOut.open("C:\\Users\\Simeon\\Desktop\\smallBanswer66666666.txt");
	int cases = 0;
	myIn >> cases;

	for (int i = 0; i < cases; i++) {
		string s;
		myIn >> s;

		MyOut << "Case #" << i + 1 << ": " << numberofnumbers(s) << endl;
	}
	return 0;
}

unsigned long long numberofnumbers(string n) {
	string k = n;
	string ss = n;
	unsigned long long k2 = stoull(k);
	bool check = false;
	sort(ss.begin(), ss.end());

	if (k2 < 10 || k == ss)
		return k2;
	else {
		while (check == false)
		{
			k2--;
			if (isnumberincreasing(k2) == false)
				break;
		}
		return k2;
	}
}

bool isnumberincreasing(unsigned long long n) {

	string temp = to_string(n);
	long size = temp.length();
	vector<char> V(size);
	vector<char> V2(size);
	bool checks = false;
	for (int i = 0; i < size; i++) {
		V[i] = temp[i];
		V2[i] = temp[i];
	}

	sort(V.begin(), V.end());

	for (int i = 0; i < size; i++) {
		if (V[i] != V2[i])
			checks = true;
	}

	if (checks == true)
		return true;
	else
		return false;
}