#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

void run()
{
    string s;
    int K;

    fin >> s >> K;

    int ans = 0;
    for (int i = 0; i + K - 1 < s.length(); i++)
    {
        if (s[i] == '-')
        {
            ans++;
            for (int j = 0; j < K; j++)
                s[i+j] = '+' + '-' - s[i+j];
        }
    }

    for (int i = 0; i < s.length(); i++)
        if (s[i] == '-')
            ans = -1;

    if (ans == -1)
        fout << "IMPOSSIBLE";
    else
        fout << ans;
}

int main()
{
    int T; fin >> T;
    for (int i = 1; i <= T; i++)
    {
        fout << "Case #" << i << ": ";
        run();
        fout << "\n";
    }
}