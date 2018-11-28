// Probleme B v1

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <cmath>
#include <map>

using namespace std;

long long puissance10(int p)
{
    long long n = 1;

    for(int i = 1; i <= p; i++)
    {
        n *= 10;
    }

    return n;
}

vector<int> toVector(long long number)
{
    vector<int> a;

    while(number != 0)
    {
        a.push_back(number % 10);
        number /= 10;
    }

    return a;
}

long long toNumber(vector<int> &a)
{
    long long retour = 0;

    for(unsigned int i = 0; i < a.size(); i++)
    {
        retour += (a[i] * puissance10(i));
    }

    return retour;
}

int main()
{
    int n;
    cin >> n;


    for(int i = 0; i < n; i++)
    {
        long long number;
        cin >> number;

        vector<int> v = toVector(number);
        vector<int> chiffreMax;
        chiffreMax.resize(v.size());

        chiffreMax.back() = 0;

        for(int i = v.size() - 2; i >= 0; i--)
        {
            chiffreMax[i] = max(chiffreMax[i+1], v[i+1]);
        }

        for(unsigned int i = 0; i < v.size(); i++)
        {
            if(chiffreMax[i] > v[i])
            {
                v[i] = 9;

                v[i+1]--;
            }
        }

        for(int i = v.size() - 2; i >= 0; i--)
        {
            v[i] = max(v[i], v[i+1]);
        }

        cout << "Case #" << i + 1  << ": " <<   toNumber(v) << endl;
    }
}
