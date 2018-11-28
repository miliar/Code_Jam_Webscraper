#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdint>
using namespace std;

int main(void)
{
	int numOfTest;
	cin >> numOfTest;
	
	for(int iOfTest=1 ; iOfTest<=numOfTest ; ++iOfTest) {
		int64_t nStall, nPeople;
		cin >> nStall >> nPeople;
		
		int64_t nStallInOdd, nStallInEven;
		int64_t nOdd, nEven;
		if(nStall % 2) nStallInOdd = nStall, nOdd = 1, nStallInEven = 0, nEven = 0;
		else nStallInEven = nStall, nEven = 1, nStallInOdd = 0, nOdd = 0;
		
		int64_t timeOfIter = std::log2(nPeople);
		int64_t nLeft = nPeople - ( (1 << static_cast<unsigned>(timeOfIter)) - 1);
		
		//cout << "iter: " << timeOfIter << " left: " << nLeft << "\n\n";
		
		while(timeOfIter--) {
			if(nOdd == 0) { // only even group
				nStallInEven /= 2; 
				if(nStallInEven % 2) nStallInOdd = nStallInEven, --nStallInEven;
				else nStallInOdd = nStallInEven - 1;
				nOdd = nEven;
			}
			else if(nEven == 0) { // only odd group
				nStallInOdd /= 2;
				if(nStallInOdd % 2) nOdd *= 2;
				else nStallInEven = nStallInOdd, nEven = nOdd * 2, nStallInOdd = 0, nOdd = 0;
			}
			else {
				int64_t _nStallInOdd, _nStallInEven;
				int64_t _nOdd, _nEven;
				
				nStallInEven /= 2;
				if(nStallInEven % 2) _nStallInOdd = nStallInEven, _nStallInEven = nStallInEven - 1,
					_nEven = _nOdd = nEven;
				else _nStallInEven = nStallInEven, _nStallInOdd = nStallInEven - 1,
					_nEven = _nOdd = nEven;
				
				nStallInOdd /= 2;
				if(nStallInOdd % 2) _nOdd += nOdd * 2;
				else _nEven += nOdd * 2;
				
				nStallInEven = _nStallInEven; nStallInOdd = _nStallInOdd; nEven = _nEven; nOdd = _nOdd;
			}
			//cout << "odd: " << nStallInOdd << '|' << nOdd << '\n' << "eve: " << nStallInEven << '|' << nEven << "\n\n";
		}
		
		cout << "Case #" << iOfTest << ": ";
		
		if( (nStallInEven > nStallInOdd && nLeft <= nEven) || 
				(nStallInOdd > nStallInEven && nLeft > nOdd) ) // use even
			cout << nStallInEven / 2 << ' ' << nStallInEven / 2 - 1;
		else // use odd
			cout << nStallInOdd / 2 << ' ' << nStallInOdd / 2;
			
		cout << endl;
	}
	
	return 0;
}
