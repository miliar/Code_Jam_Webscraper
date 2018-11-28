#include <functional>
#include <iostream>
#include <limits>
#include <queue>

void testcase(int n)
{
    std::priority_queue<unsigned long long> q;
    unsigned long long s = 0;
    unsigned long long k = 0;
    std::cin>>s;
    std::cin>>k;
    q.push(s);
    unsigned long long l,r;
    for (unsigned long long i = 0; i < k; ++i)
    {
        unsigned long long max = q.top();
        q.pop();
        unsigned long long pos = (max + 1)/2;
        l = pos - 1;
        r = max - pos;
        q.push(l);
        q.push(r);
    }

    std::cout<<"Case #"<<n<<": "<<r<<" "<<l<<std::endl;
}

int main()
{
    int N;
    std::cin>>N;
    for (auto n = 1; n <= N; ++n)
        testcase(n);

    std::cout.flush();
    return 0;
}
