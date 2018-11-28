#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

pair<long, long> solve(long N, long K);

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);
    srand(time(NULL));

    if(!file)
        return -1;

    int T = 0;
    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        long N, K;
        file >> N >> K;
        
        pair<long, long> maxmin = solve(N, K);

        output << "Case #" << i+1 << ": " << maxmin.first << " " << maxmin.second << endl;
    }

    file.close();
    output.close();

    return 0;
}


pair<long, long> solve(long N, long K)
{
    map<long, long> groups;
    groups[N] = 1;
    long left, right;

    while (K > 0)
    {
        long maxGroup = groups.rbegin()->first;
        long nbIn = groups[maxGroup];
        K -= nbIn;

        left = (maxGroup-1)/2;
        right = ceil((maxGroup - 1) / 2.0);
        groups.erase(maxGroup);
        groups[left] += nbIn;
        groups[right] += nbIn;
    }

    pair<long, long> maxmin(right, left);
    return maxmin;
}

