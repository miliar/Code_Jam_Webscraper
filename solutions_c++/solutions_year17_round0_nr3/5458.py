#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define DEBUG  0

using namespace std;

void cal(const int stall, const int people)
{
	vector<bool> line(stall+2, false);

	line[0] = true;
	line[line.size() - 1] = true;


	int maxMinDis = -1;
	int maxDis = -1;

	for (int i = 0; i < people; i++) {
		int idx = -1;
		maxMinDis = -1;
		maxDis = -1;

		for (int j = 1; j < (1 + stall); j++) {
			if (line[j])
				continue;

			/* cur min dis */
			int k = j-1;
			for (; k >= 0; k--)
				if (line[k])
					break;
			int leftDis = j - k - 1;

			k = j+1;
			for (; k < line.size(); k++)
				if (line[k])
					break;
			int rightDis = k - j - 1;

			int curMinDis = (leftDis <= rightDis) ? leftDis : rightDis;
			//cout << leftDis << " " << rightDis << " " << curMinDis << endl;
			int curMaxDis = (leftDis > rightDis) ? leftDis : rightDis;

			bool blReplace = false;
			if (curMinDis > maxMinDis) {
				blReplace = true;
			} else if (curMinDis == maxMinDis) {
				if (curMaxDis > maxDis)	{
					blReplace = true;
				}	
			}

			if (blReplace) {
				idx = j;
				maxMinDis = curMinDis;
				maxDis = curMaxDis;
			}
		}

		line[idx] = true;
	}

	cout << maxDis << " " << maxMinDis << endl;
}

int main()
{
	ifstream File;
	File.open("/Users/lester/Downloads/C-small-1-attempt0.in");
	//File.open("/Users/lester/Downloads/A-large.in");
	//File.open("./test.in");

	if (!File.is_open()) {
		cout << "faild" << endl;
		return 0;
	}

	int Times = -1;

	File >> Times;
	//cout << Times << endl;

	for (int i = 1; i <= Times; i++) {
		int stall;
		int people;

		File >> stall >> people;

#if DEBUG
		cout << "====== #"<< i << "======" << endl;
		cout << stall << " " << people << endl;
#endif
		cout << "Case #" << i << ": ";
		cal(stall, people);
		//cout << endl;
		//cout << "Case #" << i << ": "<< cal(stall, people) << endl;
	}

	return 0;
}
