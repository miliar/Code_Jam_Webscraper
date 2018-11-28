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

char reverse (char c)
{
    if (c - '+' == 0)
        return '-';
    return '+';
}

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
        string s;
        cin >> s;
        int step, numberOfReverse = 0;
        cin >> step;
        for (int j = 0; j < s.length() - step + 1; j++)
        {
            if (s[j] - '-' == 0)
            {
                for (int k = 0; k < step; k++)
                    s[j + k] = reverse(s[j + k]);
                numberOfReverse++;
            }
        }
        bool OK = true;
        for (int j = s.length() - step + 1; j < s.length(); j++)
            if (s[j] - '-' == 0)
                OK = false;
        if (OK)
            cout << numberOfReverse << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;//Your program should return 0 on normal termination.
}
