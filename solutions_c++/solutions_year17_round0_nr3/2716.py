#include <iostream>
#include <queue>
#include <unordered_map>

void addStalls(long long size, long long amount, std::priority_queue<long long>& q, std::unordered_map<long long, long long>& m)
{
    if (m.find(size) == m.end())
    {
        m.insert(std::pair<long long, long long>(size, amount));
        q.push(size);
    }
    else
    {
        m[size] += amount;
    }
}

long long doStuff(long long N, long long K)
{
    std::priority_queue<long long> q;
    q.push(N);
    std::unordered_map<long long, long long> m;
    m.insert(std::pair<long long, long long>(N, 1));
    --K;
    
    /*std::cout << "QUEUE" << std::endl;
    std::cout << N << ", " << 1 << std::endl;*/
    while (K > 0)
    {
        long long top = q.top();
        long long amount = m[top];
        K -= amount;
        m.erase(top);
        if (K >= 0)
        {
            q.pop();
        }
        
        long long leftSize;
        if (top % 2 == 0)
        {
            leftSize = top / 2 - 1;
        }
        else
        {
            leftSize = top / 2;
        }

        addStalls(leftSize, amount, q, m);

        long long rightSize = top / 2;
        addStalls(rightSize, amount, q, m);

 /*       std::priority_queue<long long> q2 = q;
        std::cout << "QUEUE" << std::endl;
        while (!q2.empty())
        {
            long long top2 = q2.top();
            q2.pop();            
            std::cout << top2 << ", " << m[top2] << std::endl;
        }*/
    }

    return q.top();
}

int main()
{
    int nTests;
    std::cin >> nTests;

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        std::cout << "Case #" << iTest << ": ";

        long long N, K;
        std::cin >> N >> K;

        long long s = doStuff(N, K);

        if (s % 2 == 0 && s > 0)
        {
            std::cout << s / 2 << " " << s / 2 - 1 << std::endl;
        }
        else
        {
            std::cout << s / 2 << " " << s / 2 << std::endl;
        }
    }

    return 0;
}