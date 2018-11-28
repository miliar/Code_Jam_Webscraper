#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define DEBUG  0

using namespace std;

int getFlipTimes(const string &line, const int size)
{
	int ans = 0;
	
	/* To bool arrary */
	vector<bool> vec;
	
	for (int i = 0; i < line.size(); i++) {
		bool blUp = ('+' == line[i]);
		vec.push_back(blUp);
	}

	/* Calculate */
	int end = vec.size() - size;
	
	for (int i = 0; i <= end; i++) {
		if (!vec[i]) {
			for (int j = 0; j < size; j++) {
				vec[i+j] = !vec[i+j];
			}
			ans++;
		}
	}

	/* Check is all up */
	for (int i = 0; i < vec.size(); i++) {
		if (!vec[i]) {
			ans = -1;
			break;
		}
	}

	return ans;
}

int main()
{
	ifstream File;
	//File.open("/Users/lester/Downloads/A-small-attempt0.in");
	File.open("/Users/lester/Downloads/A-large.in");
	//File.open("./test.in");

	if (!File.is_open()) {
		cout << "faild" << endl;
		return 0;
	}

	int Times = -1;

	File >> Times;
	//cout << Times << endl;

	for (int i = 1; i <= Times; i++) {	
		string line;
		int size;

		File >> line >> size;

#if DEBUG
		cout << "====== #"<< i << endl;
		cout << line << " " << size << endl;
		
		cout << getFlipTimes(line, size) << endl;
#endif
		int ans = getFlipTimes(line, size);

		if (0 <= ans)
			cout << "Case #" << i << ": "<< ans << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
