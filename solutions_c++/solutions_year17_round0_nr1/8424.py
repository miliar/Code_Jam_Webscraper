#include <bits/stdc++.h>

using namespace std;

int sol(string pancake, int K)
{
    int counter = 0;

    for(int i = 0; i < pancake.size(); i++)
    {
        if(pancake[i] == '-')
        {
            if(i > pancake.size() - K)
                return -1;

            counter++;
            for(int j = i; j < i+K; j++)
            {
                if(pancake[j] == '-')
                    pancake[j] = '+';
                else if(pancake[j] == '+')
                    pancake[j] = '-';
            }
        }
    }

    return counter;
}

int T;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        int K;
        string pancake;
        cin >> pancake >> K;

        int soluzione = sol(pancake, K);

        if(soluzione == -1)
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i+1 << ": " << soluzione << endl;
    }

    return 0;
}
