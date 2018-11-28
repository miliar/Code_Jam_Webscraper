#include <bits/stdc++.h>

using namespace std;

typedef int64_t i64;

class range
{
public:
    i64 dim;
    i64 num;
    range(i64 d, i64 n)
    {
        dim = d;
        num = n;
    }
    bool operator<(const range& o) const
    {
        return dim > o.dim;
    }
};

int main()
{
    int t;
    cin >> t;
    for(int caso = 1; caso <= t; caso++)
    {
        i64 tot, steps;
        cin >> tot >> steps;
        steps--;
        set<range> s;
        s.insert(range(tot, 1));
        while(steps > 0)
        {
            auto tmp = *s.begin();
            s.erase(s.begin());
            if(steps < tmp.num)
            {
                tmp.num -= steps;
                steps = 0;
                s.insert(tmp);
            }
            else
            {
                steps -= tmp.num;
                auto insert = [&s](const range& r) {
                    if(s.count(r))
                    {
                        auto it = s.find(r);
                        auto tmprng = *it;
                        s.erase(it);
                        tmprng.num += r.num;
                        s.insert(tmprng);
                    }
                    else
                    {
                        s.insert(r);
                    }
                };
                if(tmp.dim > 1)
                {
                    if(tmp.dim % 2 == 1)
                    {
                        insert(range(tmp.dim / 2, tmp.num * 2));
                    }
                    else
                    {
                        insert(range(tmp.dim / 2, tmp.num));
                        if(tmp.dim > 3)
                            insert(range(tmp.dim / 2 - 1, tmp.num));
                    }
                }
            }
        }
        auto tmp = *s.begin();
        cout << "Case #" << caso << ": ";
        if(tmp.dim % 2 == 1)
            cout << tmp.dim / 2 << " " << tmp.dim / 2;
        else
            cout << tmp.dim / 2 << " " << tmp.dim / 2 - 1;
        cout << endl;
    }
    return 0;
}
