#include <iostream>

using namespace std;

int main()
{
    int testcases = 0;
    int k;
   
    cin >> testcases;
   int testcase = 1;
    while (testcase <= testcases) {
        int tidy = false;
        cin >> k;
        int number = k;
        int currentNumber = number;
        while(tidy == false && currentNumber >= 0) {
            int temp = currentNumber;
            int last_digit = temp%10;
            temp /= 10;
            tidy = true;
            
            while (temp > 0) {
                int digit = temp%10;
                temp /= 10;
                if (last_digit < digit) {
                    tidy = false;
                    currentNumber--;
                    break;
                }
                last_digit = digit;
            }
        }
        cout<<"Case #"<< testcase <<": " << currentNumber<<endl;
        testcase++;
    }
   return 0;
}
