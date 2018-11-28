#include <iostream>
#include <string>
#include <vector>

using namespace::std;

/* used to accommodate for would-be calculations on huge numbers */
unsigned long long handleLargeInput(unsigned long long x)  
{  
    if(x >= 111111111111111110) {
        return 99999999999999999;
    } else if(x >= 11111111111111110) {
        return 9999999999999999;
    } else if(x >= 1111111111111110) {
        return 999999999999999;
    } else if(x >= 111111111111110) {
        return 99999999999999;
    } else if(x >= 11111111111110) {
        return 9999999999999;
    } else if(x >= 1111111111110) {
        return 999999999999;
    } else if(x >= 111111111110) {
        return 99999999999;
    } else if(x >= 11111111110) {
        return 9999999999;
    } else if(x >= 1111111110) {
        return 999999999;
    } else if (x >= 111111110) {
        return 99999999;
    } else if (x >= 11111110) {
        return 9999999;
    } else {
        return 999999;
    }
}

bool isTidy(unsigned long long num) {
    
    int dig;
    int prevDig = -1;
    while (num > 0)
    {
        dig = num % 10;
        if(prevDig != -1 && dig > prevDig) {
            return false;
        }
        num /= 10;
        prevDig = dig;
    }
    
    return true;
}

int main()
{
    int t;
    unsigned long long int k;
    vector<unsigned long long int> nums;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> k;
        nums.push_back(k);
    }
    
    int i=1;
    for(auto n: nums) {
        cout << "Case #" << i << ": ";
        if(n >= 1111110) {
            if(!isTidy(n)) {
                n = handleLargeInput(n);
            }
        } else {
            while(!isTidy(n)) {
                n--;
            }
            i++;
        }
        cout << n << endl;
    }
}