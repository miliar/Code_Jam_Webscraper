#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>
#include <ios>

using namespace std;

namespace
{
    using Val = unsigned int;
    using Flt = double;

    struct Cand
    {
        Val pos;
        Val speed;
    };

    using CandCol = vector<Cand>;

    Flt maxSpeed(const CandCol &cands, Val dst)
    {
        auto maxTime = 0.0;
        for(const auto &c : cands)
        {
            const auto t = static_cast<Flt>(dst - c.pos)/c.speed;
            maxTime = max(t, maxTime);
        }
        return dst/maxTime;
    }
}

int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0; i < t; ++i)
    {
        Val d = 0;
        int n = 0;
        cin>>d>>n;
        CandCol cands;
        while(n-- > 0)
        {
            CandCol::value_type c{};
            cin>>c.pos>>c.speed;
            cands.push_back(c);
        }
        const auto res = maxSpeed(cands, d);
        cout.precision(6);
        cout<<"Case #"<<i+1<<": "<<fixed<<res<<endl;
    }
    return 0;
}
