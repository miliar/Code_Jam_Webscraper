#include <iostream>
#include <vector>
#include <ios>
#include <algorithm>
#include <cmath>
#include <set>
#include <numeric>

using namespace std;

namespace
{
    struct Cake
    {
        int r;
        int h;
    };

    using uint = unsigned int;
    using CakeCol = vector<Cake>;

    double area(const CakeCol &cakes, uint k)
    {
        using HeightSet = multiset<double>;
        CakeCol sortedCakes(cakes);
        sort(begin(sortedCakes), end(sortedCakes),
            [](const Cake &left, const Cake &right) {
                return left.r < right.r || (left.r ==right.r && left.h < right.h);
            });
        double maxArea = 0.0;
        HeightSet heights;
        for(const auto &c : sortedCakes)
        {
            const auto add = 2.0*M_PI*c.r*c.h;
            if(heights.size() == k-1)
            {
                const auto prevAdd = accumulate(begin(heights), end(heights), 0.0);
                const auto area = M_PI*c.r*c.r + add + prevAdd;
                if(area > maxArea)
                    maxArea = area;
                heights.insert(add);
                heights.erase(begin(heights));
            }
            else
            {
                heights.insert(add);
            }
        }
        return maxArea;
    }
}

int main()
{
    int t = 0;
    cin>>t;
    for(int i =0; i < t; ++i)
    {
        int n = 0;
        int k =0;
        cin>>n>>k;
        CakeCol cakes;
        for(int j = 0; j < n; ++j)
        {
            Cake c{0, 0};
            cin>>c.r>>c.h;
            cakes.push_back(c);
        }
        const auto r = area(cakes, k);
        cout.precision(7);
        cout<<"Case #"<<i+1<<": "<<fixed<<r<<endl;
    }
    return 0;
}
