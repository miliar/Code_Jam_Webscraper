#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string.h>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
//
//int calculate(string str, int size)
//{
//    
//}

bool isTidy(long long x)
{
    long long temp = x;
    int digit = temp % 10;
    temp = temp /10;
    while (temp > 0)
    {
//        if(temp % 10 == 0)
//            temp = temp / 10;
//        else
//        {
            if(digit < (temp % 10))
                return false;
            else
                digit = temp % 10;
            temp = temp / 10;
//        }
    }
    return true;
}

long long lastTidy(long long x)
{
    long long y = x;
    while (y > 0)
    {
        if(isTidy(y))
            return y;
        
        y--;
    }
    return 0;
}


int main() {
    int t;
    long long m;
    //string n;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> m;  // read n and then m.
        cout << "Case #" << i << ": "<<lastTidy(m)<< endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    
    return 0;
}