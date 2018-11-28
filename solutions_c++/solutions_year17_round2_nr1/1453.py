#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
using namespace std;

void SolveTest(ifstream& in, ofstream& out);

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int T;
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        out << "Case #" << t + 1 << ": ";
        SolveTest(in, out);
    }

    return 0;
}

void SolveTest(ifstream& in, ofstream& out)
{
    int D, N;
    in >> D >> N;

    vector<int> positions(N);
    vector<int> speeds(N);

    for (int i = 0; i < N; ++i)
    {
        int K, S;
        in >> K >> S;

        positions[i] = K;
        speeds[i] = S;
    }

    double maxSpeed = numeric_limits<double>::max();

    for (int i = 0; i < N; ++i)
    {
        int distance = D - positions[i];
        double mySpeed = (double)D * speeds[i] / distance;
        maxSpeed = min(maxSpeed, mySpeed);
    }

    out << setprecision(12) << maxSpeed << endl;
}