#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <iomanip>
#include <utility>
#include <iterator>
#include <set>
#include <map>
using namespace std;

void subtractOne(char *str, int len)
{
    if (str[len - 1] != '0') {
        int digit = str[len - 1] - '0';
        digit--;
        str[len - 1] = digit + '0';
    }
    else {
        str[len - 1] = 9 +'0';
        subtractOne(str, len - 1);
    }
}
bool isIncreasingHelper(char *str, int len)
{
    for (size_t i = 0; i < len; i++)
    {
        if (str[i] > str[i + 1])
            return false;
    }
    return true;
}

bool isIncreasing(char *str, int len)
{
    for (int i = 0; i < len - 1; i++)
    {
        if (str[i] > str[i + 1]) {
            int digit = str[i] - '0';
            digit--;
            str[i] = digit + '0';
            for (int j = i + 1; j < len; j++)
            {
                str[j] = '9';
            }
        }
        
    }
    if (!isIncreasingHelper(str, len))
        isIncreasing(str, len - 1);
    return true;
}
int main(void)
{
    char input[27];
    int T, N;
    cin >> T;
    for (size_t i = 0; i < T; i++)
    {
        cin >> input;
        int len = strlen(input);
        isIncreasing(input, len);
        cout << "Case #" << (i + 1) << ": ";
        bool firstZero = true;
        for (int j = 0; j < len; j++) {
            if (firstZero && input[j] == '0') {
                //firstZero = false;
                continue;
            }
            else {
                firstZero = false;
                cout << input[j];
            }
        }
        cout << endl;
    }
	return 0;
}