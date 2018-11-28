#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<int> partition(long n)
{
    vector<int> result;

    long divider = 10;
    while (n / divider) {
        long rest = n % divider;
        long part = rest / (divider / 10);
        result.insert(result.begin(), part);

        divider *= 10;
    }
    long rest = n % divider;
    long part = rest / (divider / 10);
    result.insert(result.begin(), part);

    return result;
}


void resetTo9sFrom(int pos, vector<int>& partitions)
{
    partitions.at(pos - 1) -= 1;

    int size = partitions.size();
    for (int i = pos; i < size; ++i) {
        partitions.at(i) = 9;
    }
}


long compose(vector<int>& partitions)
{
    long result = 0;

    long multiplier = pow(10, partitions.size() - 1);
    for (auto p : partitions) {
        result += p * multiplier;
        multiplier /= 10;
    }

    return result;
}


long findAnswer(long n)
{
    if (n < 10) {
        return n;
    }

    vector<int> partitions = partition(n);
    int size = partitions.size();
    for (int i = size - 1; i > 0; --i) {
        if (partitions.at(i) < partitions.at(i-1)) {
            resetTo9sFrom(i, partitions);
        }
    }

    return compose(partitions);
}


int main(int argc, char* argv[])
{
    int t;
    cin >> t;

    long n;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << findAnswer(n) << endl;
    }

    return 0;
}
