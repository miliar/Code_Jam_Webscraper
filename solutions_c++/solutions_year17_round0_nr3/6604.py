#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string input = "5 4 2 5 2 6 2 1000 1000 1000 1";
    stringstream ss(input);
    int t;
    ss >> t;
    for (int i = 1; i <= t; ++i)
    {
        long long int n;
        long long int k;
        ss >> n >> k;
        cout << "Case #" << i << ": ";
        priority_queue<long long int> intervals;
        intervals.push(n);
        for (long long int j = 1; j < k; ++j)
        {
            long long int longestInterval = intervals.top();
            intervals.pop();
            if (longestInterval / 2 > 0)
                intervals.push(longestInterval / 2);
            if ((longestInterval - 1) / 2 > 0)
                 intervals.push((longestInterval - 1) / 2);
        }
         long long int longestInterval = intervals.top();
         cout << longestInterval / 2 << " " << (longestInterval - 1) / 2 << endl; 
    }
}