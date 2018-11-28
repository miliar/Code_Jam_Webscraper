#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <fstream>

using namespace std;

string per(long long N)
{
    string s;
    while (N > 0)
    {
        s.push_back(N % 10 + '0');
        N /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

int main()
{
    ofstream fout("lol.in");
    ifstream fin("kek.in");
    long long N, T;
    string ans;
    fin >> T;
    for (long long i = 0; i < T; ++i)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> N;
        ans = per(N);
        long long j = 0;
        while (j < ans.size() - 1 && ans[j] <= ans[j + 1])
        {
            ++j;
        }
        if (j == ans.size() - 1 && ans[j - 1] <= ans[j])
            fout << ans << endl;
        else
        {
            long long num = j;
            if (ans[j] == '1')
            {
                while (num > 0)
                {
                    ans[num] = '9';
                    --num;
                }
                for (long long k = j + 1; k < ans.size(); ++k)
                {
                    ans[k] = '9';
                }
                ans.erase(0 + ans.begin());
            }
            else
            {
                long long hop = ans[j], num = j;
                while (num > 0 && ans[num - 1] == hop)
                {
                    ans[num] = '9';
                    --num;
                }
                ans[num] -= 1;
                for (long long k = j + 1; k < ans.size(); ++k)
                {
                    ans[k] = '9';
                }
            }
            fout << ans << endl;
        }
    }
    fin.close();
    fout.close();
}
