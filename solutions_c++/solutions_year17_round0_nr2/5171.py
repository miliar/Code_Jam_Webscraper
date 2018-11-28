#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int NR;
    cin >> NR;

    ll temp;
    vector<int> nb;

    for(int q = 0; q < NR; q++)
    {
        nb.clear();

        cin >> temp;

        do
        {
            nb.push_back(temp % 10);
            temp /= 10;
        } while(temp != 0);

        reverse(nb.begin(), nb.end());

        bool found = true;
        while(found)
        {
            found = false;

            for(int i = 0; i < nb.size() - 1; i++)
            {
                if(nb[i] > nb[i + 1])
                {
                    nb[i] -= 1;

                    for(int j = i + 1; j < nb.size(); j++)
                    {
                        nb[j] = 9;
                    }
                    found = true;
                    break;
                }
            }
        }

        cout << "Case #" << (q + 1) << ": ";
        int first = 0;
        for(int i = 0; i < nb.size() - 1; i++)
        {
            if(nb[i] == 0)
                first++;
            else
                break;
        }

        for(int i = first; i < nb.size(); i++)
            cout << nb[i];
        cout << endl;
    }


    return 0;
}
