#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
using namespace std;


int main()
{
    int cases;
    cin >> cases;
    for(int i = 1; i <= cases; ++i)
    {
        double destination;
        int horse_number;
        cin >> destination >> horse_number;
        double max_time = 0;
        for(int j = 0; j < horse_number; ++j)
        {
            int loc, speed;
            double time;
            cin >> loc;
            cin >> speed;
            time = (destination - loc) / speed;
            if(time > max_time)
            {
                max_time = time;
            }
        }
        cout.precision(17);
        cout << "Case #" << i << ": " << fixed << (destination / max_time) << "\n";
    }
    return 0;
}