//
//  main.cpp
//  C
//
//  Created by Volodymyr Polosukhin on 22/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

const long double INF = 1e18;
const long double EPS = 1e-12;

long double answer;

void smallPreprocess(const vector < long long > &e, const vector < long long > &s, const vector < vector < long long > > &d)
{
    vector < long long > totalDistance(d.size());
    
    totalDistance[0] = 0;
    for (int i = 1; i < (int)d.size(); ++i)
    {
        totalDistance[i] = totalDistance[i-1] + d[i-1][i];
    }
    
    vector<long double> dp(d.size(), INF);
    
    dp[0] = 0.0L;
    
    for (int i = 1; i < (int)d.size(); ++i)
    {
        for (int j = i-1; j >= 0; --j)
        {
            long long path = totalDistance[i] - totalDistance[j];
            
            if (e[j] >= path)
            {
                dp[i] = min(dp[j] + 1.0L * path / s[j], dp[i]);
            }
        }
    }
    
    answer = dp.back();
}

long double smallSolve(int from, int to)
{
    return answer;
}

vector < vector < long double > > graph;

void largePreprocess(const vector < long long > &e, const vector < long long > &s, vector < vector < long long > > d)
{
    const int n = (int)d.size();
    
    for (int k=0; k<n; ++k)
        for (int i=0; i<n; ++i)
            for (int j=0; j<n; ++j)
                if (d[i][k] != -1 && d[k][j] != -1 &&
                    (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]))
                {
                    d[i][j] = d[i][k] + d[k][j];
                }
    
    graph.assign(n, vector < long double > (n, -1));
    
    for (int i =0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (d[i][j] != -1 && d[i][j] <= e[i])
            {
                graph[i][j] = 1.0L * d[i][j] / s[i];
            }
        }
    }
    
    for (int k=0; k<n; ++k)
        for (int i=0; i<n; ++i)
            for (int j=0; j<n; ++j)
                if (graph[i][k] > -EPS && graph[k][j] > -EPS &&
                    (graph[i][j] < -EPS || graph[i][j] > graph[i][k] + graph[k][j]))
                {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
}

long double largeSolve(int from, int to)
{
    return graph[from][to];
}

int main(int argc, const char * argv[]) {
//    freopen("C-small-attempt0.in.txt", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);
    
    
    freopen("C-large.in.txt", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    cout.precision(9);
    cout.setf(ios::fixed);
    
    int t;
    cin >> t;
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        int n, q;
        
        cin >> n >> q;
        
        vector < long long > e(n), s(n);
        
        for (int i = 0; i < n; ++i)
        {
            cin >> e[i] >> s[i];
        }
        
        vector < vector < long long > > d(n, vector < long long > (n));
        
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j< n; ++j)
            {
                cin >> d[i][j];
            }
        }
        
        largePreprocess(e, s, d);
        
        cout << "Case #" << testcase << ": ";
        
        for (int i = 0; i < q; ++i)
        {
            int u, v;
            
            cin >> u >> v;
            
            cout << largeSolve(u-1, v-1) << ' ';
        }
        
        cout << endl;
    }
    
    return 0;

}
