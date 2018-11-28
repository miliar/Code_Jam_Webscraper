#include <iostream>
#include <set>
#include <algorithm>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <sstream>
using namespace std;
struct numbers
{
    long long v;
    long long n;
};
void testf(numbers &n1, numbers &n2)
{
    numbers temp1 = n1;
    numbers temp2 = n2;
    if (n1.v % 2 == 0)
    {
        n1.v = ceil((temp1.v - 1) / 2.0);
        n1.n = temp1.n;
        n2.v = floor((temp1.v - 1) / 2.0);
        n2.n = temp2.n * 2 + temp1.n;
    }
    else
    {
        n1.v = (temp1.v - 1) / 2;
        n1.n = temp1.n * 2 + temp2.n;
        n2.v = n1.v - 1;
        n2.n = temp2.n;
    }
     //cout << n1.v << ":" << n1.n << " " << n2.v << ":" << n2.n << endl;
}
void functions()
{
    long long thesize, n;
    cin >> thesize >> n;
    numbers n1 = {thesize, 1};
    numbers n2 = {0, 0};
    long long powr = floor(log2(n));
    for (int i = 0; i < powr; ++i)
    {
        testf(n1, n2);
    }
    if (n - pow(2, powr) < n1.n)
    {
        int output1 = ceil((n1.v - 1) / 2.0);
        if (output1 < 0)
            cout << 0;
        else
            cout << output1;
        int output2 = floor((n1.v - 1) / 2.0);

        cout << " ";

        if (output2 < 0)
            cout << 0;
        else
            cout << output2;
        cout << endl;
    }
    else
    {
        int output1 = ceil((n2.v - 1) / 2.0);
        if (output1 < 0)
            cout << 0;
        else
            cout << output1;
        int output2 = floor((n2.v - 1) / 2.0);

        cout << " ";

        if (output2 < 0)
            cout << 0;
        else
            cout << output2;
        cout << endl;
    }
}
int main()
{
    //    cout << n1.v << ":" << n1.n << " " << n2.v << ":" << n2.n << endl;

    int n;
    cin >> n;
    for (int i = 1; i < n + 1; ++i)
    {
        cout << "Case #" << i << ": ";
        functions();
    }
}