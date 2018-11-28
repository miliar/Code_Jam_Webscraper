#include <algorithm>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;

#define PRINT

#define TASKNUM "A"
#define DATASET "small"

ifstream fsIn(TASKNUM "-" DATASET "-practice.in.txt");
ofstream fsOut(TASKNUM "-" DATASET "-practice.out.txt");

class TTestCase
{
private:
    long Result;

    int N, P;
    vector<int> G;

    vector<int> g;

    void Load();
    bool Solve();
    void Check();

    bool _ResultBool;
public:
    TTestCase();
    ~TTestCase();
};


void TTestCase::Load()
{
    cin >> N >> P;
    G.resize(N);
    g.resize(P);
    for (int i = 0; i < N; ++i) {
        cin >> G[i];
        ++g[G[i] % P];
    }
}

bool TTestCase::Solve()
{
    if (P == 3)
        Result = g[0] + min(g[1], g[2]) + (max(g[1], g[2]) - min(g[1], g[2])) / 3 + ((max(g[1], g[2]) - min(g[1], g[2])) % 3? 1 : 0);
    else if (P == 2)
        Result = g[0] + g[1] / 2 + (g[1] % 2? 1: 0);
    return true;
}




void TTestCase::Check()
{
}

TTestCase::TTestCase()
{
    Load();

    _ResultBool = Solve();
}

TTestCase::~TTestCase()
{
    Check();
    cout << Result << " ";
    fsOut << Result << " ";
    cout << endl;
    fsOut << endl;
}


int main()
{
    if (!fsIn.is_open())
    {
        cout << "No input file found";
    }
    cin.rdbuf(fsIn.rdbuf());

    int numberOfCases;
    cin >> numberOfCases;

    for (int caseNum = 1; caseNum <= numberOfCases; ++caseNum)
    {
        TTestCase testCase;

        cout << "Case #" << caseNum << ": ";
        fsOut << "Case #" << caseNum << ": ";
    }

    cout << "Finished";
    for (;;);
    return 0;
}
