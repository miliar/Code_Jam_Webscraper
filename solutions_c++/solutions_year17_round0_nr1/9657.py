#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
	int isComplete = 1, flipCount=0;
	std::ifstream input("A-large.in");
	std::ofstream output("T1_output.txt");
	std::string str, testCaseCount;
	std::string file_contents;
	std::getline(input, testCaseCount);
	int count = 0;
	while (std::getline(input, str))
	{
		string buf; // Have a buffer string
		stringstream ss(str); // Insert the string into a stream
		vector<string> tokens; // Create vector to hold our words
		while (ss >> buf)
			tokens.push_back(buf);

		flipCount = 0;
		isComplete = 1;
		for (std::string::size_type i = 0; i < str.size(); i++) {
			if (str[i] == '-') {
				isComplete = 0;
				if ((i + stoi(tokens[1]) + 1) < str.size()) {
					flipCount++;
					isComplete = 1;
					for (int j = 0; j < stoi(tokens[1]); j++) {
						if (str[i + j] == '-') {
							str[i + j] = '+';
						}
						else {
							str[i + j] = '-';
						}
						
					}
				}
			}
		}
		if (isComplete == 0) {
			output << "Case #" << (++count) << ": IMPOSSIBLE" << "\n";
		}
		else {
			output << "Case #" << (++count) << ": " << flipCount << "\n";
		}
	}

	input.close();
	output.close();

	return 0;
}