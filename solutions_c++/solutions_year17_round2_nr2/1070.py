#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;
typedef double flt;

int cnt[6];
int ar[6] = { 1, 3, 2, 6, 4, 5 };
char chr[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };

bool isValid(int a, int b)
{
    return (ar[a] & ar[b]) == 0;
}

void print(int test_number, string str)
{
    cout << "Case #" << test_number << ": " << str << endl;
}

void solve(int test_number)
{
    int n;
    cin >> n;
    for (int q = 0; q < 6; ++q)
        cin >> cnt[q];
    
    /*
    if (test_number == 3)
    {
        print(test_number, "YBRGRB");
        return;
    } // */
    
    vector<int> result;
    for (int q = 0; q < 6; ++q)
        if (cnt[q] != 0)
        {
            result.push_back(q);
            --cnt[q];
            break;
        }
    
    for (int q = 1; q < n; ++q)
    {
        int maxVal = 0, maxIndex = -1;
        for (int i = 0; i < 6; ++i)
        {
            if (isValid(result.back(), i) and cnt[i] > maxVal)
            {
                maxVal = cnt[i];
                maxIndex = i;
            }
        }
//        cout << q << endl;
        if (maxIndex == -1)
        {
            print(test_number, "IMPOSSIBLE");
            return;
        }
        else
        {
            result.push_back(maxIndex);
            --cnt[maxIndex];
        }
    }
    if (not isValid(result[0], result.back()))
    {
        print(test_number, "IMPOSSIBLE");
        return;
    }
    
    string res;
    for (int x : result)
    {
        res += chr[x];
    }
    print(test_number, res);
}

int main()
{
//  /*
    freopen("btest.in", "r", stdin);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
