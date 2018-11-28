#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

std::vector<int> digits;
std::ofstream myoutput("output.txt");
static unsigned long long count = 0;

bool checkIfTidyNumber(unsigned long long num) {
    std::vector<int> dig;
    unsigned long long x = num;
	while(x) {
		dig.push_back(x%10);
		x = x/10;
	}
	int n = dig.size();
	if(n <= 1)
        return true;
	for(int i = n-1; i >= 1; --i){
        if(dig[i] > dig[i-1])
            return false;
	}
	return true;
}
unsigned long long returnTidyNumber(unsigned long long num, int n) {
	unsigned long long tidyNum = 0;
	if(n <= 1)
		return num;
    unsigned long long temp = digits[n-1] * pow(10, n-1);
	if(digits[n-1] <= digits[n-2]){
		tidyNum = temp + returnTidyNumber(num - temp, n-1);
		digits.pop_back();
	} else {
        tidyNum = temp - 1;
	}
    return tidyNum;
}

int main() {
	//int num = 100;

    std::fstream file("input.txt");
    unsigned long long t, num, x, result;

    file >> t;
    while(t){
        file >> num;
        result = num;

        while(!checkIfTidyNumber(result)) {
            digits.clear();
            x = result;
            while(x) {
                digits.push_back(x%10);
                x = x/10;
            }
            result = returnTidyNumber(result, digits.size());
        }
        t--;
        myoutput <<"Case #"<<++count<<": "<< result << std::endl;
	}

	return 0;
}


