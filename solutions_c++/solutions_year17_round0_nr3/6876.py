#include <iostream>
#include <vector>
using namespace std;
int main() {
	int num = 0;
	int numb = 0;
	int a = 0;
	int b = 0;
	int peep = 0;
	int d = 0;
	int count = 0;
	int count1 = 1;
	int f = 0;
	int max = 0;
	int min = 0;
	int temp = 0;
	int temp1 = 0;
	vector<int>stall;

	cin >> num;
	int number[num*2];
	for (int a = 0; a < num; a++) {
		cin >> numb;
		cin >> peep;
		max = numb;
		for (int b = 0; b < peep; b++) {
			 temp=(max-1)/2;
			 temp1 = max;
			temp1 /= 2;
			 stall.push_back(temp1);
			stall.push_back (temp);
			if (b == (peep - 1)) {
				max = temp1;
				min = temp;
				
				break;
			}
			max = 0;
			for (int q = 0; q < stall.size(); q++) {
				if (stall[q] > max) {
					max = stall[q];
					count = q;
				}
			}
			stall.erase(stall.begin() + count);

		}
		stall.clear();
		number[f] = max;
		number[f + 1] = min;
		f += 2;
	
	}
	for (int w = 0; w < num*2; w+=2) {
		cout << "Case #" << count1 << ": " << number[w] << " " << number[w + 1]<< endl;
		count1++;
	}
	return 0;
}