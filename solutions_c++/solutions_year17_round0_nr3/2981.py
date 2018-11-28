#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;

void push(vector<long long> &v, long long n)
{
    v.push_back((n-1)/2);
    v.push_back(n/2);
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long t, test_case;
    cin >> test_case;
    for(long long t = 1; t <= test_case; t++)
    {
        cout << "Case #" << t << ": ";

        long long n, k;
        cin >> n >> k;

        long long l = 0;
        long long s = 1;
        long long sum = 0;
        while(true)
        {
            if(k > s)
            {
                l++;
                k -= s;
                sum += s;
            }
            else
                break;
            s *= 2;
        }
        long long y = 0;
        n -= sum;
        long long x = pow(2,l);
        long long r = n%x;
        long long q = n/x;
        if(k > r)
            y = q;
        else
            y = q + 1;
        cout << max(y/2, (y-1)/2) << " " << min(y/2, (y-1)/2) << endl;
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}