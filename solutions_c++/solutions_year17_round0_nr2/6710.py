#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cmath>
using namespace std;

void tidynum(unsigned long long number, int caseNum) {
	int length = 0;
	unsigned long long n = number;
        for(; n!=0; n/=10, length++);	
	int * result = new int[length];

	for(int i = 0; i < length; i++) {
		result[length-i-1] = (number/(unsigned long long)pow(10,i))%10;
	}

	for(int j = length-1; j >=0; j--)
	{
		if(result[j] < result[j-1])
		{
			result[j-1] --;
			for(int jj = j; jj < length; jj++) 
				result[jj] = 9;
		}
	}
	
	cout << "Case #" << caseNum << ": ";
	for(int q = 0; q < length; q++)
	{
		if(!(q == 0 && result[q] == 0))
			cout << result[q];
	}
	cout << endl;


}


int main() {

	int testNum;
	string line;

/*test code start
	string numStr = ull_to_str(1234567891234567898);
	cout << ull_to_str(1234567891234567898) << endl;
	cout << tidynum(numStr) << endl;
test code end
*/
//	tidynum(123456789123456789, 1);

	ifstream myfile("B-large.in");
	
	if (myfile.is_open()) {
		getline (myfile, line);	//get test number
		istringstream iss(line);
		iss >> testNum;
		//cout << testNum << endl;
		int count = 0;
		while ( getline (myfile, line)) {	//get and parse the rest
			istringstream istr(line);
			unsigned long long num;
			istr >> num;
			count += 1;
			tidynum(num, count);	//call tidynum
		}
		myfile.close();

	}

	return 0;
}

