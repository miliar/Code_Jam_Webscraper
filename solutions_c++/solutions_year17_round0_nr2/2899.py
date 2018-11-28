#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<set>
//#define cin in
//#define cout out
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");


void printCase (int number)
{
    cout << "Case #" << number << ": ";
}

int main()
{
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; i++)
    {
        printCase(i + 1);
        string number;
        cin >> number;
        int nineFrom = number.length();
        for (int j = number.length() - 2; j >= 0; j--)
        {
            if (number[j] > number[j + 1])
            {
                number[j]--;
                nineFrom = j + 1;
            }
        }
        for (int j = nineFrom; j < number.length(); j++)
            number[j] = '9';
        if (number[0] - '0' == 0)
            number.erase(0, 1);
        cout << number << endl;
    }
    return 0;//Your program should return 0 on normal termination.
}
