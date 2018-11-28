#include <vector>
#include <iostream>

using namespace std;

int main()
{
    long long n, k;
    cin >> n >> k;
    vector<int> bits;
    vector<int> tots;
    long long bit = 1;
    long long tot = 1;
    while(bit <= n)
    {
        bits.push_back(bit);
        tots.push_back(tot);
        bit *= k;
        tot += bit;
    }
    long long answer = 0;
    for(int i=0; i<bits.size() && n > 0; i++)
    {
        int idx = bits.size()-i-1;
        if(n >= tots[idx])
        {
            long long quot = n / tots[idx];
            n -= quot * tots[idx];
            answer += quot * bits[idx];
        }
    }
    cout << answer << endl;
}
