#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

std::vector<int> digits;
std::ofstream myoutput("output.txt");
static int count = 0;

bool checkIfTidyNumber(int num) {
    std::vector<int> dig;
    int x = num;
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
int returnTidyNumber(int num, int n) {
	//int n = digits.size();
	int tidyNum = 0;
	if(n <= 1)
		return num;
	if(digits[n-1] <= digits[n-2]){
		int temp = digits[n-1] * pow(10, n -1);
		tidyNum = temp + returnTidyNumber(num - temp, n-1);
		digits.pop_back();
	} else {
		int x = digits[n-1] - 1;
		if (x > 0){
			tidyNum = (digits[n-1] * pow(10, n-1)) - 1;
		} else {
			tidyNum = returnTidyNumber((digits[n-1] * pow(10, n-1)) - 1, n-1);
		}
	}
    return tidyNum;
}

int main() {
	//int num = 100;

    std::fstream file("input.txt");
    unsigned long long t, num, x;

    file >> t;
    while(t){
        file >> num;
        x = num;
        digits.clear();
        while(x) {
            digits.push_back(x%10);
            x = x/10;
        }

        int result = returnTidyNumber(num, digits.size());
        if(!checkIfTidyNumber(result)) {
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


