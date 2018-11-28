#include <iostream>
#include <algorithm>
#include <array>
#include <string>
#include <set>
#include <utility>
#include <functional>
#include <cassert>

using namespace std;

namespace
{
    using Val = unsigned int;
    constexpr Val COLOR_CNT = 6;
    using CntAr = array<Val, COLOR_CNT>;
    using ColAr = array<char, COLOR_CNT>;
    constexpr ColAr COLORS = {'R', 'O', 'Y', 'G', 'B', 'V'};
    constexpr CntAr CODES = {1, 1+2, 2, 2+4, 4, 1+4};
    constexpr CntAr DEPS= {3, 0, 5, 0, 1, 0};

    inline Val colorIdx(char c)
    {
        auto aIter = find(begin(COLORS), end(COLORS), c);
        assert(aIter != end(COLORS));
        const auto aIdx = aIter - begin(COLORS);
        return aIdx;
    }

    inline bool accept(char a, char b)
    {
        const auto aIdx = colorIdx(a);
        const auto bIdx = colorIdx(b);
        return (CODES[aIdx] & CODES[bIdx]) == 0;
    }

    struct Cand
    {
        Val count;
        char c;
    };

    inline bool isComp(char c)
    {
        return c == 'O' || c == 'G' || c == 'V';
    }

    bool operator<(const Cand &a, const Cand &b)
    {
        return
            (a.count > b.count ||
             (a.count == b.count &&
              (a.c < b.c)));
    }

    string places(CntAr &counts, Val s)
    {
        using CntSet = multiset<Cand>;
        string res;
        CntSet rest;
        for(Val i = 0; i < counts.size(); ++i)
        {
            if(counts[i] > 0 && !isComp(COLORS[i]))
            {
                rest.insert(Cand{counts[i], COLORS[i]});
            }
        }
        while(!rest.empty())
        {
            auto iter = begin(rest);
            Val maxCount = 0;
            Val firstCount = 0;
            auto firstIter = end(rest);
            bool found = false;
            if(!res.empty())
            {
                for(auto sIter = begin(rest); sIter != end(rest); ++sIter)
                {
                    const auto &p = *sIter;
                    maxCount = max(maxCount, p.count);
                    if(p.c == res.front())
                    {
                        firstCount = p.count;
                        firstIter = sIter;
                    }
                }
                assert(maxCount > 0);
                if(maxCount == firstCount && accept(res.back(), firstIter->c))
                {
                    iter = firstIter;
                    found = true;
                }
            }
            if(!found)
            {
                while(iter != end(rest) && (!res.empty() && !accept(res.back(), iter->c)))
                {
                    ++iter;
                }
            }
            if(iter == end(rest))
            {
                return string();
            }
            const auto val = iter->c;
            auto cnt = iter->count;
            assert(cnt > 0);
            rest.erase(iter);
            res.push_back(val);
            --cnt;
            const auto depIdx = DEPS[colorIdx(val)];
            if(counts[depIdx] > 0 && cnt > 0)
            {
                --counts[depIdx];
                res.push_back(COLORS[depIdx]);
                res.push_back(val);
                --cnt;
            }
            if(cnt > 0)
            {
                rest.insert(Cand{cnt, val});
            }
        }
        for(Val i = 0; i < counts.size(); ++i)
        {
            if(counts[i] > 0 && isComp(COLORS[i]))
            {
                if(counts[i] > 1)
                    return string();
                if(!res.empty() && !accept(res.back(), COLORS[i]))
                    return string();
                res.push_back(COLORS[i]);
            }
        }
        if(res.size() > 1 && !accept(res.front(), res.back()))
        {
            return string();
        }
        return res;
    }
}
int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0; i < t; ++i)
    {
        Val s = 0;
        cin>>s;
        CntAr counts;
        for(Val i = 0; i < COLOR_CNT; ++i)
        {
            Val n = 0;
            cin>>n;
            counts[i] = n;
        }
        const auto res = places(counts, s);
        cout<<"Case #"<<i+1<<": "<<(!res.empty()?res:"IMPOSSIBLE")<<endl;
    }
    return 0;
}
