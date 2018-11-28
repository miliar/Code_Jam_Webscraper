#include <iostream>
#include <set>
#include <algorithm>
#include <cmath>
#include <string>
#include <iomanip>
#include <sstream>
using namespace std;
void functions()
{
    string input;
    cin >> input;
    int thesize = input.size();
    for (int i = 0; i < thesize - 1; ++i)
    {
        if (input[i] > input[i + 1])
        {
            if (input[i] != '0')
                input[i] -= 1;
            else
                input[i] = '9';
            for (int j = i + 1; j < thesize; ++j)
                input[j] = '9';
            i = 0;
        }
    }
    for (int i = 0; i < thesize - 1; ++i)
    {
        if (input[i] > input[i + 1])
        {
            if (input[i] != '0')
                input[i] -= 1;
            else
                input[i] = '9';
            for (int j = i + 1; j < thesize; ++j)
                input[j] = '9';
            i = 0;
        }
    }
    stringstream ss;
    long long output;
    ss << input;
    ss >> output;

    cout << output << endl;
}
int main()
{
    int n;
    cin >> n;
    for (int i = 1; i < n + 1; ++i)
    {
        cout << "Case #" << i << ": ";
        functions();
    }
}