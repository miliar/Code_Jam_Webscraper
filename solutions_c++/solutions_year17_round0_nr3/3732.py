#include<iostream>
#include<map>

using namespace std;

int main()
{
    int T;
    long long int N, K;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        long long int Ls, Rs;
        map<long long int, long long int> m;
        cin >> N >> K;
        m[N] = 1;
        for(int j = 0; j < K; ++j)
        {
            auto rit = m.rbegin();
            if((rit -> first) & 1)
            {
                if(((rit -> first) >> 1) != 0) m[((rit -> first) >> 1)] += 2;
                if(j == (K - 1))
                {
                    Ls = (rit -> first) >> 1;
                    Rs = (rit -> first) >> 1;
                }
            }
            else
            {
                if(((rit -> first) >> 1) != 0) m[((rit -> first) >> 1)]++;
                if((((rit -> first) >> 1) - 1) != 0) m[((rit -> first) >> 1) - 1]++;
                if(j == (K - 1))
                {
                    Ls = ((rit -> first) >> 1) - 1;
                    Rs = (rit -> first) >> 1;
                }
            }
            m[rit -> first]--;
            if(m[rit -> first] == 0) m.erase(rit -> first);
        }
        cout << "Case #" << i << ": " << Rs << ' ' << Ls << endl;
    }
    return 0;
}
