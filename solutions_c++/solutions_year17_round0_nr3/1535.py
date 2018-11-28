#include <fstream>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;
long long n, k;
long long leftSize, rightSize;

void computeDistances()
{
    unordered_map<long long, long long> spaces;
    priority_queue<long long> biggestSpace;
    spaces[n] = 1;
    biggestSpace.push(n);
    long long people = 0;
    long long spaceSize, numberOfSpaces;
    while (!biggestSpace.empty())
    {
        spaceSize = biggestSpace.top();
        biggestSpace.pop();
        numberOfSpaces = spaces[spaceSize];
//        spaces.erase(spaces.find(spaceSize));
        if (spaceSize % 2 == 0)
        {
            rightSize = spaceSize >> 1;
            leftSize =  rightSize - 1;
        }
        else
        {
            leftSize = rightSize = spaceSize >> 1;
        }
        if (spaces.find(leftSize) == spaces.end())
        {
            spaces[leftSize] = 0;
            biggestSpace.push(leftSize);
        }
        if (spaces.find(rightSize) == spaces.end())
        {
            spaces[rightSize] = 0;
            biggestSpace.push(rightSize);
        }
        spaces[leftSize] += numberOfSpaces;
        spaces[rightSize] += numberOfSpaces;
        people += numberOfSpaces;
        if (people >= k)
        {
            break;
        }
    }
}


int main()
{
    int t;
    ifstream f("stalls.in");
    ofstream g("stalls.out");
    f >> t;
    for (int i = 0; i < t; i++)
    {
        f >> n >> k;
        computeDistances();
        g << "Case #" << i + 1 << ": " << max(leftSize, rightSize) << " " << min(leftSize, rightSize) << '\n';
    }
    f.close();
    g.close();
    return 0;
}