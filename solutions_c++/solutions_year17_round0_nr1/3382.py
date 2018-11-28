#include <iostream>
#include <string>
using namespace std;

int main(){

	int dataNum = 0;
	cin >> dataNum;
	for (int i = 1; i <= dataNum; i++){
		string pancakes;
		int flipNum = 0;
		cin >> pancakes;
		cin >> flipNum;

		int pancakeLength = pancakes.length();
		int recentScore = 0;
		int flipCount = 0;
		for (int c = 0; c < pancakeLength; c++){
			// cout << pancakes[c];
			if (pancakes[c] == '+')
				recentScore += 1;
		}
		// cout << flipNum << endl;

		int cookPosition = 0;
		while(recentScore < pancakeLength && cookPosition <= pancakeLength - flipNum){
			if (pancakes[cookPosition] == '-'){
				for (int a = 0; a < flipNum; a++){
					if (pancakes[cookPosition + a] == '+'){
						pancakes[cookPosition + a] = '-';
						recentScore--;
					}else{
						pancakes[cookPosition + a] = '+';
						recentScore++;
					}
				}
				flipCount++;
			}
			cookPosition++;
		}

		if (recentScore != pancakeLength)
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << flipCount << endl;

	}

	return 0;
}