#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    int nbT;
    cin >> nbT;

    int nb;
    int K;
    for (int t = 1; t <= nbT; t++)
    {
        string crepes;
        cin >> crepes >> K;
        nb = crepes.size();
        int res = 0;
        for (int i = 0; i <= nb-K; i++)
        {
            if (crepes[i] == '-')
            {
                res++;
                for (int j = i; j < i+K; j++)
                {
                    if (crepes[j] == '+')
                        crepes[j] = '-';
                    else
                        crepes[j] = '+';
                }
            }

        }

        bool isOk = true;
        for (int i = 0; i < nb; i++)
        {
            if (crepes[i] == '-')
            {
                isOk = false;
                break;
            }
        }




        std::cout << "Case #" << t << ": ";
        if (!isOk)
            std::cout << "IMPOSSIBLE\n";
        else
            std::cout << res << "\n";
    }
    return 0;
}
