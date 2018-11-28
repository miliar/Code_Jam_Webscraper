#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
using namespace std;

void SolveTest(int t, ifstream& in, ofstream& out);

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int T;
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        out << "Case #" << t + 1 << ": ";
        SolveTest(t, in, out);
    }

    return 0;
}

struct SResource
{
    int distance;
    int speed;
};

struct Investigation
{
    int from;
    int to;
};

void Travel(int from, SResource currentResource, const vector<vector<int>>& gameMap, const vector<SResource>& resources, double& bestTimeSoFar, double travelTime);

void SolveTest(int t, ifstream& in, ofstream& out)
{
    int N, Q;
    in >> N >> Q;
    vector<SResource> resources(N);
    for (int i = 0; i < N; ++i)
    {
        int E, S;
        in >> E >> S;
        resources[i] = SResource{ E, S };
    }

    vector<vector<int>> gameMap(N);
    for (int i = 0; i < N; ++i)
    {
        gameMap[i].resize(N);
        for (int j = 0; j < N; ++j)
        {
            int D;
            in >> D;
            gameMap[i][j] = D;
        }
    }
    vector<Investigation> investigations(Q);
    for (int i = 0; i < Q; ++i)
    {
        int U, V;
        in >> U >> V;
        investigations[i] = Investigation{ U, V };
    }


    // Small data set
    double bestTimeSoFar = numeric_limits<double>::max();
    Travel(0, SResource{ 0, 0 }, gameMap, resources, bestTimeSoFar, 0.0);

    out << setprecision(12) << bestTimeSoFar << endl;
}

void Travel(int from, SResource currentResource, const vector<vector<int>>& gameMap, const vector<SResource>& resources, double& bestTimeSoFar, double travelTime)
{
    int lastCity = gameMap.size() - 1;
    if (from == lastCity)
    {
        bestTimeSoFar = min(bestTimeSoFar, travelTime);
        return;
    }

    double travelTimeWithSwitch = numeric_limits<double>::max();
    double travelTimeWithoutSwitch = numeric_limits<double>::max();

    int distance = gameMap[from][from + 1];
    if (currentResource.distance >= distance)
    {
        currentResource.distance -= distance;
        travelTimeWithoutSwitch = (double)distance / currentResource.speed;
        if (travelTime + travelTimeWithoutSwitch < bestTimeSoFar)
        {
            Travel(from + 1, currentResource, gameMap, resources, bestTimeSoFar, travelTime + travelTimeWithoutSwitch);
        }
    }

    currentResource = resources[from];
    if (currentResource.distance >= distance)
    {
        currentResource.distance -= distance;
        travelTimeWithSwitch = (double)distance / currentResource.speed;
        if (travelTime + travelTimeWithSwitch < bestTimeSoFar)
        {
            Travel(from + 1, currentResource, gameMap, resources, bestTimeSoFar, travelTime + travelTimeWithSwitch);
        }
    }
}