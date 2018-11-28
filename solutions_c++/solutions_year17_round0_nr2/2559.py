#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    int nbT;
    cin >> nbT;


    for (int t = 1; t <= nbT; t++)
    {
        string nb;
        cin >> nb;
        int size = nb.size();

        int i = 0;
        while (i != size-1 && nb[i] <= nb[i+1])
            i++;
        if (i != size-1)
        {
            while (i != 0 && nb[i] == nb[i-1])
                i--;
            nb[i]--;
            i++;
            while (i != size)
            {
                nb[i] = '9';
                i++;
            }
        }



        if (nb[0] == '0')
        {
            nb.erase(0,1);

        }

        std::cout << "Case #" << t << ": " << nb << '\n';
    }
    return 0;
}
