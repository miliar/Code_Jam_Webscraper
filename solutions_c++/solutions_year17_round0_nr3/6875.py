#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

//void updateMax(int personNumber, std::vector<int>& stalls, std::vector<int>& occupiedPositions) {
//	std::sort(occupiedPositions.begin(), occupiedPositions.end());
//	int lPos = 0, rPos = 0, pos = 0;
//	int Ls = 0, Rs = 0;
//	int maxDiff, diff;
//	maxDiff = diff = 0;
//	for (auto i = 0; i < occupiedPositions.size() - 1; ++i) {
//		lPos = occupiedPositions[i];
//		rPos = occupiedPositions[i+1];
//		pos = (rPos - lPos) / 2;
//		Ls = pos - lPos;
//		Rs = rPos - pos;
//		diff = (Ls <= Rs) ? Ls : Rs;
//		if (diff > maxDiff)
//			maxDiff = diff;
//	}
//	occupiedPositions[personNumber] = pos;
//	std::cout << personNumber << "\t" << maxDiff << std::endl;
//}
void insertPerson(unsigned long long personNumber, std::vector<unsigned long long>& stalls, unsigned long long& max, unsigned long long& min) {
	int l = 0, r = 0;
	int lMax = 0, rMax = 0;
	int diff = 0, maxDiff = 0;
	for (int i = 0; i < stalls.size(); ++i) {
		//Find first occurence of 1
		if (stalls[i]) {
			r = i;
			diff = r - l;
			if (diff > maxDiff) {
				if (l > lMax)
					lMax = l;
				if (r > rMax)
					rMax = r;
				maxDiff = diff;
			}
			l = r;
		}

	}
	int pos = lMax + (rMax - lMax) / 2;

	max = rMax - pos - 1;
	min = pos - lMax - 1;
	stalls[pos] = 1;
}
int main() {	
	std::fstream file("input.txt");
	std::ofstream myoutput("output.txt");
	unsigned long long K, N, t, i, j, max, min;

	file >> t;
	j = t;
	while (j) {
		file >> N >> K;
		std::vector<unsigned long long> stalls(N + 2, 0);
		//std::vector<int> occupiedPositions(K+2, 0);

		stalls[0] = stalls[N + 1] = 1; // occupied by guards
		//occupiedPositions[0] = 0;
		//occupiedPositions[1] = N + 1;

		i = max = min = 0;
		while (i < K) {
			//updateMax(i, stalls, occupiedPositions);
			insertPerson(i, stalls, max, min);
			++i;
		}
		//std::cout << max << "\t" << min << std::endl;
		
		myoutput << "Case #" << (t-j+1) << ": " << max << " " << min << std::endl;
		j--;
	}
	
}