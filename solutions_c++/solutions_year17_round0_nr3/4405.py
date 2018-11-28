#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void num(int N, int K, int& y, int& z)
{
    priority_queue<int> pq;
    pq.push(N);

    for (int i = 0; i < K - 1; ++i)
    {
        int top = pq.top();
        pq.pop();

        pq.push(top / 2);
        pq.push((top - 1) / 2);
    }

    int top = pq.top();
    y = top / 2;
    z = (top - 1) / 2;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;

        int K;
        cin >> K;

        int y, z;
        num(N, K, y, z);
        cout << "Case #" << i + 1 << ": " << y << " " << z << endl;
    }
}