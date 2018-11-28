#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        int d, n;
        cin >> d >> n;

        double temps = 0;

        for(int j = 0; j < n; j++)
        {
            int k, s;
            cin >> k >> s;


            temps = max(temps, ((double)d - (double)k) / (double)s);
        }
        printf("Case #%d: %f\n", i+1,(double)d / (double)temps);
        //cout << (double)d / temps << endl;
    }



    return 0;
}























