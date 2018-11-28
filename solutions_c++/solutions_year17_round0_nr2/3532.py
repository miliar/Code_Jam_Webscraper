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
		string numStr;
		cin >> numStr;
		
		auto itOfFinished = numStr.end();
		while(true) {
			auto it = numStr.begin() + 1;
			char lastChar = numStr.front();
			for( ; it!=itOfFinished ; ++it) {
				if(*it < lastChar) break;
				lastChar = *it;
			}
			if(it == itOfFinished) break;
			
			--*(it-1);
			for(; it!=itOfFinished ; ++it) *it = '9';
		}
		if(numStr.front() == '0') numStr = string(numStr.size()-1, '9');
		
		cout << "Case #" << iOfTest << ": ";
		cout << numStr;
		cout << endl;
	}
	
	return 0;
}
