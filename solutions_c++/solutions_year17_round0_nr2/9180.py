#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <cassert>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

unsigned long getSolution(unsigned long n);
bool isTidy(unsigned long n);

int main(int argc, char *argv[])
{
    int NUM_LINES;
    unsigned long number;
    cin >> NUM_LINES;
    for(int i = 1; i <= NUM_LINES; ++i)
    {
        cin >> number;
        //cout << "Case #" << i << ": " << number << endl;

        unsigned long result = getSolution(number);
        cout << "Case #" << i << ": ";
        cout << result;
        cout << endl;
    }

    return 0;
}

unsigned long getSolution(unsigned long number)
{
    assert(number >= 1);
    unsigned long n(number);

    const std::string s = to_string(n);
    std::string ss(s);
    sort(ss.begin(), ss.end());

    while(ss[0] < s[0])
    {
        ss.erase(0, 1);
        ss += '#'; // adding # to the end so we could have equal length
    }

    //cout << "s=" << s << " ss=" << ss << endl;

    if(isTidy(n))
        return n;

    int start_index = 0;
    for(int i = 0; i < s.length(); ++i)
    {
        if(s[i] != ss[i])
        {
            // check if previous digit is not the same
            start_index = i - 1;
            while(start_index > 0 && s[start_index] == s[start_index-1])
            {
                start_index--;
            }

            break;
        }
    }

    //cout << " n=" << n << " start_index=" << start_index << endl;
    unsigned long n1 = n;
    unsigned long mod = -1;
    if(start_index > 0)
    {
        mod = pow(10, s.length() - start_index);
        n1 = n / mod;
        n = n % mod;
    }

    //int result = -1;
    for(unsigned long i = n - 1; i > 0; --i)
    {
        if(isTidy(i))
        {
            //cout << "FOUND " << i << " n1%10="<< n1%10 << " i/(mod/10)=" << i/(mod/10) <<  endl;

            if(i % 10 == 9 &&  n1%10 > i/(mod/10) && start_index > 0)
            {
                // we need to handle -1 on previous numbers ;(
                int p1 = s.length() - 1;
                unsigned long pow_result = pow(10, p1);
                int base = static_cast<int>(number / pow_result) - 1;
                unsigned long result = base * pow_result + (pow_result - 1);
                //cout << "result is " << result << " base="<< base << endl;
                return result;

            }
            return start_index > 0 ? n1 * mod + i : i;
        }
    }
    return -1;
}

bool isTidy(unsigned long n)
{
    int last_digit = 99;
    //cout << "TESTCASE FOR " << n << endl;
    while(n % 10 <= last_digit && n/10 != 0)
    {
        last_digit = n % 10;
        n /= 10;
        //cout << "n=" << n << endl;
    }
    return (n / 10 == 0 && n <= last_digit);
}
