#include <iostream>
#include <vector>
#include <set>

using namespace std;

void solve();

class fraction
{
    long long num, div;
    void normalize()
    {
        long long a = num;
        long long b = div;
        while(a && b)
            if(a < b)
                b %= a;
            else
                a %= b;
        num /= (a | b);
        div /= (a | b);
    }
public:
    fraction(int a)
    {
        num = a;
        div = 1;
    }
    fraction(int a, int b)
    {
        num = a;
        div = b;
        normalize();
    }
    fraction operator+(const fraction& other) const
    {
        return fraction(num * other.div + div * other.num, div * other.div);
    }
    fraction operator*(const fraction& other) const
    {
        return fraction(num * other.num, div * other.div);
    }
    fraction operator-() const
    {
        return (*this) * -1;
    }
    fraction operator/(const fraction& other) const
    {
        return fraction(num * other.div, div * other.num);
    }
    fraction operator+() const
    {
        return *this;
    }
    fraction operator-(const fraction& other) const
    {
        return (*this) + (-other);
    }
};

int main()
{
    int t;
    cin >> t;
    cout.precision(15);
    for(int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ':';
        cerr << "Case #" << i << " of " << t << endl;
        solve();
    }
    return 0;
}

void calc_horseways(int n, vector<pair<int, int> >* roads, int start, double speed, int max_dist, vector<pair<int, double> >* horseways)
{
    double max_time = max_dist / speed;
    double times[n];
    for(int i = 0; i < n; i++)
        times[i] = 1. / 0;
    set<pair<double, int> > dijkstra;
    times[start] = 0;
    dijkstra.insert(make_pair(0., start));
    while(!dijkstra.empty())
    {
        pair<double, int> cur = *dijkstra.begin();
        dijkstra.erase(dijkstra.begin());
        if(times[cur.second] != cur.first)
            continue;
        horseways[start].push_back(make_pair(cur.second, cur.first));
        for(int i = 0; i < roads[cur.second].size(); i++)
        {
            double new_time = cur.first + roads[cur.second][i].second / speed;
            if(new_time > max_time || new_time >= times[roads[cur.second][i].first])
                continue;
            times[roads[cur.second][i].first] = new_time;
            dijkstra.insert(make_pair(new_time, roads[cur.second][i].first));
        }
    }
}

void solve()
{
    int n, q;
    cin >> n >> q;
    pair<int, int> horses[n];
    for(int i = 0; i < n; i++)
        cin >> horses[i].first >> horses[i].second;
    vector<pair<int, int> > roads[n];
    vector<pair<int, double> > horseways[n];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
        {
            int s;
            cin >> s;
            if(i != j && s >= 0)
                roads[i].push_back(make_pair(j, s));
        }
    for(int i = 0; i < n; i++)
        calc_horseways(n, roads, i, horses[i].second, horses[i].first, horseways);
    for(int i = 0; i < q; i++)
    {
        int start, end;
        cin >> start >> end;
        set<pair<double, int> > dijkstra;
        double times[n];
        for(int i = 0; i < n; i++)
            times[i] = 1. / 0;
        times[start - 1] = 0;
        dijkstra.insert(make_pair(0., start - 1));
        while(!dijkstra.empty())
        {
            pair<double, int> cur = *dijkstra.begin();
            dijkstra.erase(dijkstra.begin());
            if(times[cur.second] != cur.first)
                continue;
            for(int i = 0; i < horseways[cur.second].size(); i++)
            {
                double new_time = cur.first + horseways[cur.second][i].second;
                if(new_time < times[horseways[cur.second][i].first])
                {
                    times[horseways[cur.second][i].first] = new_time;
                    dijkstra.insert(make_pair(new_time, horseways[cur.second][i].first));
                }
            }
        }
        cout << ' ' << times[end - 1];
    }
    cout << endl;
}
