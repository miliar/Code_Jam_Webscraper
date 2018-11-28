#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int b, d;
int initialHealth;

struct State{
    int hd, ad, hk, ak;
    State() : hd(0), ad(0), hk(0), ak(0){}
    State(int _hd, int _ad, int _hk, int _ak) : hd(_hd), ad(_ad), hk(_hk), ak(_ak){}

    State strike()const
    {
        return State(hd, ad, max(0, hk - ad), ak);
    }

    State counterStrike()const
    {
        return State(max(0, hd - ak), ad, hk, ak);
    }

    State buff()const
    {
        return State(hd, ad + b, hk, ak);
    }

    State debuff()const
    {
        return State(hd, ad, hk, max(0, ak - d));
    }

    State cure()const
    {
        return State(initialHealth, ad, hk, ak);
    }

    bool win()const
    {
        return hk == 0;
    }

    bool lose()const
    {
        return hd == 0;
    }

    void scan()
    {
        scanf("%d%d%d%d", &hd, &ad, &hk, &ak);
    }

    bool operator<(const State & other)const
    {
        if (hd != other.hd)
            return hd < other.hd;
        if (ad != other.ad)
            return ad < other.ad;
        if (hk != other.hk)
            return hk < other.hk;
        return ak < other.ak;
    }
};

map<State, int> dist;
queue<State> que;

void tryAdd(State now, int d)
{
    if (!now.lose() && dist.find(now) == dist.end())
    {
        dist[now] = d;
        que.push(now);
    }
}

int solve()
{
    dist.clear();
    while (!que.empty())
        que.pop();
    State start;
    start.scan();
    initialHealth = start.hd;
    scanf("%d%d", &b, &d);
    dist[start] = 0;
    que.push(start);
    while (!que.empty())
    {
        State cur = que.front();
        int curDist = dist[cur];
        que.pop();

        //strike & counterStrike
        State att = cur.strike();
        if (att.win())
        {
            return curDist + 1;
        }
        State now = att.counterStrike();
        tryAdd(now, curDist + 1);
        
        //buff & counterStrike
        now = cur.buff().counterStrike();
        tryAdd(now, curDist + 1);

        //debuff & counterStrike
        now = cur.debuff().counterStrike();
        tryAdd(now, curDist + 1);

        //cur & counterStrike
        now = cur.cure().counterStrike();
        tryAdd(now, curDist + 1);
    }
    return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        int res = solve();
        if (res >= 0)
            printf("Case #%d: %d\n", i + 1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
    }
    return 0;
}