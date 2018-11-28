#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int numOfTest;
	cin >> numOfTest;
	
	for(int iOfTest=1 ; iOfTest<=numOfTest ; ++iOfTest) {
		string str; int lenOfFlippper;
		cin >> str >> lenOfFlippper;
		
		const int numOfCake = str.size();
		vector<bool> pattern(numOfCake); transform(str.cbegin(), str.cend(), pattern.begin(), 
			[](char ch) -> bool { return ch == '+' ? true : false; });
		vector<bool> isEndOfFlipInterval(numOfCake+1, false);
		bool curFlipped = false;
		int numOfFlip = 0;
		
		for(int iOfCake=0, end=numOfCake-lenOfFlippper+1 ; iOfCake < end ; ++iOfCake) {
			if(isEndOfFlipInterval[iOfCake]) curFlipped = !curFlipped;
			if(!(pattern[iOfCake] ^ curFlipped)) {
				curFlipped = !curFlipped;
				++numOfFlip;
				isEndOfFlipInterval[iOfCake + lenOfFlippper] = true;
			}
		}
		bool isImpossible = false;
		for(int iOfCake = numOfCake-lenOfFlippper+1 ; iOfCake < numOfCake ; ++iOfCake) {
			if(isEndOfFlipInterval[iOfCake]) curFlipped = !curFlipped;
			if(!(pattern[iOfCake] ^ curFlipped)) { isImpossible = true; break; }
		}
		
		cout << "Case #" << iOfTest << ": ";
		if(isImpossible) cout << "IMPOSSIBLE";
		else cout << numOfFlip;
		cout << endl;
	}
	
	return 0;
}
