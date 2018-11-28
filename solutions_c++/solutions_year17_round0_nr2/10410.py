#include <iostream>
#include <string>
#include <fstream>

using namespace std;


int main()
{
	int t;
	cin >> t;
	ofstream output;
	output.open("output.txt");

	for (int j = 1; j <= t; j++) {
		long long s;
		cin >> s;
		bool tidy = false;
		if (s > 10 || s < -10) {
			while (!tidy) {
				string temp = to_string(s);
				char current = temp[0];
				for (long long i = 1; i < temp.length(); i++) {
					if (temp[i] < current) {
						s--;
						break;
					}
					else if (i == temp.length() - 1 && temp[i] >= current) {
							tidy = true;
							break;
					}
					current = temp[i];
				}
			}
		}
		output << "Case #" << j << ": " << s << endl;
	}
	output.close();
    return 0;
}

