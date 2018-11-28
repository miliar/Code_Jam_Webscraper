#include <algorithm>
#include <iostream>
#include <string>
#include <cstdint>
#include <cstring>
#include <utility>
#include <vector>

int getLS(const std::vector<bool>& stals, int s)
{
    int i = 0;
    for(s = s - 1; s >= 0; --s, i++)
        if(stals[s])
            break;

    return i;
}

int getRS(const std::vector<bool>& stals, int s)
{
    int i = 0;
    for(s = s + 1; s < stals.size(); ++s, ++i)
        if(stals[s])
            break;

    return i;
}

int getMin(std::vector<std::pair<int, int> >& LRS)
{
    int min = 0;
    int index = 0;
    for(int i = 0; i < LRS.size(); ++i)
    {
        if(LRS[i].first == -1) continue;

        int currMin = std::min(LRS[i].first, LRS[i].second);
        if(currMin > min)
        {
            min = currMin;
            index = i;
        }
        else if(currMin == min && index == 0)
            index = i;
    }

    return index;
}

int g_max;
int g_min;

int getMin2(std::vector<std::pair<int, int> >& LRS)
{
    int min = 0;
    for(int i = 0; i < LRS.size(); ++i)
    {
        if(LRS[i].first == -1) continue;

        int currMin = std::min(LRS[i].first, LRS[i].second);
        if(currMin > min)
            min = currMin;
    }

    std::vector<int> indexes;
    for(int i = 0; i < LRS.size(); ++i)
    {
        if(LRS[i].first == -1) continue;

        int currMin = std::min(LRS[i].first, LRS[i].second);
        if(currMin == min)
        {
            indexes.push_back(i);
        }
    }

    int max = 0;
    for(int i = 0; i < indexes.size(); ++i)
    {
        int currMax = std::max(LRS[indexes[i]].first, LRS[indexes[i]].second);
        if(currMax > max)
            max = currMax;
    }

    g_min = min;
    g_max = max;

    if(indexes.size() == 1)
        return indexes[0];

    std::vector<int> maxes;
    for(int i = 0; i < indexes.size(); ++i)
    {
        int currMax = std::max(LRS[indexes[i]].first, LRS[indexes[i]].second);
        if(currMax == max)
            maxes.push_back(indexes[i]);
    }

    return maxes[0];
}

std::pair<uint32_t, uint32_t> calcStals(uint32_t N, uint32_t K)
{
    std::vector<bool> stals;
    stals.resize(N+2, false);
    stals[0] = stals[N+1] = true;

    std::vector<std::pair<int, int> > LRS;
    LRS.resize(N+2, std::make_pair(-1, -1));

    for(int i = 0; i < K; ++i)
    {
        for(int s = 1; s <= N; ++s)
        {
            if(stals[s])
                continue;

            int LS = getLS(stals, s);
            int RS = getRS(stals, s);

            LRS[s] = std::make_pair(LS, RS);
        }

        int s = getMin2(LRS);

        stals[s] = true;
/*
        for(int i = 0; i < stals.size(); ++i)
            std::cout << (stals[i] ? "o" : ".");
        std::cout << std::endl;
*/
        if(i == K-1)
            return std::make_pair(g_max, g_min);

        LRS[s] = std::make_pair(-1, -1);
    }

    return std::make_pair(0, 0);
}

int main(int argc, char* argv[])
{
    int T = 0;
    std::cin >> T;

    for(int i = 0; i < T; ++i)
    {
        uint32_t N, K;
        std::cin >> N >> K;
        auto p = calcStals(N, K);
        std::cout << "Case #" << i+1 << ": " << p.first << " " << p.second << std::endl;
    }

    return 0;
}

