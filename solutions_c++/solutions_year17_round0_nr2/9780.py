#include <iostream>
#include <vector>

int main (int argc, char *argv[])
{

    int numTestCases = 0;
    std::cin >> numTestCases;
    std::vector<long int> testCases;
    long int testCase;
    for (int i=0; i < numTestCases; ++i) {
        std::cin >> testCase;
        testCases.push_back(testCase);
    }

    
    int nl = 0; 
    for(std::vector<long int>::iterator it = testCases.begin(); it != testCases.end(); ++it) {

    nl++;
    //long int number = 1111111111111111110;
    long int number = *it;

    long int mod1 = 0;
    long int mod2 = 0;

    bool isTidy = false;

    for (; number >=0; number--) {

        long int temp1 = number;
        long int calc_divides = 0;
            
        mod1 = temp1 % 10;
        temp1 = temp1 / 10;

        if (temp1 == 0) isTidy = true;

        while (temp1) {
            mod2 = temp1 % 10;
            temp1 = temp1 / 10;
            calc_divides++;

            if (mod2 > mod1) {
                isTidy = false;
                break;
            }
            else {
                isTidy = true;
            }

            mod1 = mod2;
        }
        
        if (isTidy) {
            std::cout << "Case #" << nl  <<": " << number << std::endl;
            break;
        }
        else {
            long int prune_num = 1;
            while (calc_divides--) prune_num = prune_num * 10;
            if (prune_num > 1) {
                number = number - (number % prune_num);
            }
        }
  
    }

    }
    return 0;
}
