#include <cassert>
#include <fstream>
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::vector;

vector<bool> toilet;

int max(int x, int y) { return x > y ? x : y; }
int min(int x, int y) { return x < y ? x : y; }

vector< vector<int> > getPossibleRanges()
{
    vector< vector<int> > possibleRanges;
    vector <int> range;
    for (vector<bool>::size_type i = 1; i < toilet.size(); i++)
    {
        if (toilet[i] == false && toilet[i - 1] == true)
        {
            if (range.size() < 2)
                range.push_back(i);
            else
            {
                possibleRanges.push_back(range);
                range.clear();
                range.push_back(i);
            }
        }
        else if (toilet[i] == true && toilet[i - 1] == false)
        {
            if (range.size() < 2)
                range.push_back(i - 1);
            else
            {
                possibleRanges.push_back(range);
                range.clear();
                range.push_back(i - 1);
            }
        }
    }
    possibleRanges.push_back(range);
    return possibleRanges;
}

int main(int argc, char* argv[])
{
    assert(argc == 3);
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    int T = 0;

    in >> T;
    cout << T << " Test cases" << endl;

    for (int i = 0; i < T; i++)
    {
        out << "Case #" << i + 1 << ": ";
        toilet.clear();
        int N, K;
        in >> N >> K;
        toilet.push_back(true);
        for (int j = 0; j < N; j++)
            toilet.push_back(false);
        toilet.push_back(true);
        for (int j = 0; j < K; j++)
        {
            vector< vector<int> > possibleRanges = getPossibleRanges();

            cout << "Possible ranges: ";
            for (vector< vector<int> >::iterator it = possibleRanges.begin(); it != possibleRanges.end(); it++)
                cout << "[" << (*it)[0] << ", " << (*it)[1] << "], ";
            cout << endl;

            int Ls = 0, Rs = 0;
            int minLsRs = 0, maxLsRs = 0;
            int best = 0;

            for (vector< vector<int> >::iterator it = possibleRanges.begin(); it != possibleRanges.end(); it++)
            {
                int pos = ((*it)[1] - (*it)[0]) / 2 + (*it)[0];
                Ls = pos - (*it)[0];
                Rs = (*it)[1] - pos;
                cout << "Ls = " << Ls << " " << "Rs = " << Rs << endl;
                if ((min(Ls, Rs) > minLsRs) || ((min(Ls, Rs) == minLsRs) && (max(Ls, Rs) > maxLsRs)))
                {
                    minLsRs = min(Ls, Rs);
                    maxLsRs = max(Ls, Rs);
                    best = pos;
                }
            }

            toilet[best] = true;

            if (j == (K - 1))
            {
                cout << "min(Ls, Rs) = " << minLsRs << " " << "max(Ls, Rs) = " << maxLsRs << endl;
                out << maxLsRs << " " << minLsRs << endl;
            }
        }
    }

    return 0;
}
