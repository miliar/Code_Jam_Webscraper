#include<stdafx.h>
#include <iostream>
#include<vector>
using namespace std;
void convertdig(vector<int>*dig, long long int n)
{
    if (n == 0)
        return;
    convertdig(dig, n / 10);
    (*dig).push_back(n % 10);
}
int main()
{
    int test;
    cin >> test;
    int test1 = 1;
    while (test--)
    {
        long long int n;
        cin >> n;
        vector<int>*dig = new vector<int>;
        convertdig(dig, n);
        int i = 0;
        while (i + 1 < (*dig).size() && (*dig)[i] <= (*dig)[i + 1])
        {
            i++;
        }
        cout << "Case #" << test1 << ": ";
        if (i + 1 == (*dig).size())
            cout << n;
        else
        {
            if ((*dig)[i] == 1)
            for (int j = 0; j < (*dig).size() - 1; j++)
                cout << "9";
            else
            {
                while (i - 1 >= 0 && (*dig)[i] == (*dig)[i - 1])
                    i--;
                int k = i - 1; (*dig)[i]--;
                while (k >= 0)
                {
                    if ((*dig)[k]>(*dig)[k + 1])
                    {
                        (*dig)[k] = (*dig)[k + 1];
                    }
                    else
                        break;
                    k--;
                }
                for (int j = 0; j <= i; j++)
                    cout << (*dig)[j];
                for (int j = i + 1; j < (*dig).size(); j++)
                    cout << "9";
            }
        }
        cout << endl;
        test1++;

    }
    return 0;
}

