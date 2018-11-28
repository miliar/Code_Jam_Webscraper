#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

typedef unsigned long long ull;
typedef signed long long ll;

int N, Q;
vector<pair<int, int> > horses;
vector<vector<int> > adjList;

long double dp[105][105];
long double solve(int i, int j);

int main()
{
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        cin >> N >> Q;

        horses.clear();
        for(int i = 0; i < N; i++)
        {
            int dist, speed;
            cin >> dist >> speed;
            horses.push_back(make_pair(dist, speed));
        }

        adjList.clear();
        for(int i = 0; i < N; i++)
        {
            vector<int> neighbors;
            for(int j = 0; j < N; j++)
            {
                int d;
                cin >> d;
                neighbors.push_back(d);
            }
            adjList.push_back(neighbors);
        }

        int temp;
        cin >> temp >> temp;

        for(int i = 0; i < 105; i++)
            for(int j = 0; j < 105; j++)
                dp[i][j] = -1;

        long double res = solve(0, 0);
        
        cout << fixed << showpoint << setprecision(6) << "Case #" << t << ": " << res << endl;
    }

    return 0;
}

long double solve(int i, int j)
{
    if(i >= N - 1) return 0;
    if(dp[i][j] != -1) return dp[i][j];

    long double res = 1e12;

    long double distFromJtoNext = 0;
    for(int k = j; k <= i; k++)
        distFromJtoNext += adjList[k][k + 1];

    if(horses[j].first >= distFromJtoNext)
    {
        long double timeOnJ = adjList[i][i + 1] / (long double) horses[j].second;
        res = min(res, timeOnJ + solve(i + 1, j));
    }

    if(horses[i].first >= adjList[i][i + 1])
    {
        long double timeOnI = adjList[i][i + 1] / (long double) horses[i].second;
        res = min(res, timeOnI + solve(i + 1, i));
    }

    dp[i][j] = res;
    return dp[i][j];
}