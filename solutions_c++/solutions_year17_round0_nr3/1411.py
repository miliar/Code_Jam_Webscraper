#include <iostream>
#include <map>
#include <functional>
#include <tuple>
#include <utility>
#include <cassert>

using namespace std;

namespace
{
    using Val = unsigned int;
    using LVal = unsigned long long int;

    tuple<LVal, LVal> lastDist(LVal n, LVal k)
    {
        using ChunkSet = map<LVal, LVal, greater<LVal>>;
        ChunkSet chunks;
        chunks.insert(make_pair(n, 1));
        k -= 1;
        while(k > 0)
        {
            if(chunks.empty())
                break;
            const auto p = *begin(chunks);
            if(k >= p.second)
            {
                chunks.erase(begin(chunks));
                k -= p.second;
            }
            else
            {
                begin(chunks)->second -= k;
                k = 0;
            }
            assert(p.first > 0);
            const auto vs = (p.first-1)/2;
            if(vs > 0)
            {
                chunks[vs] += p.second;
            }
            const auto vb = (p.first-1) - vs;
            if(vb > 0)
            {
                chunks[vb] += p.second;
            }
        }
        if(!chunks.empty())
        {
            auto iter = begin(chunks);
            assert(iter->first > 0);
            const auto vs = (iter->first-1)/2;
            const auto vb = (iter->first-1) - vs;
            return make_tuple(vb, vs);
        }
        else
        {
            return make_tuple(0, 0);
        }
    }
}

int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0; i < t; ++i)
    {
        LVal n = 0;
        LVal k = 0;
        cin>>n>>k;
        const auto r = lastDist(n, k);
        cout<<"Case #"<<i+1<<": "<<get<0>(r)<<' '<<get<1>(r)<<endl;
    }
    return 0;
}
