#include <iostream>
#include <cstdio>

using namespace std;

int NR;


int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    cin >> NR;

    string temp;
    int k, s;
    bool pancakes[1000];
    for(int q = 0; q < NR; q++)
    {
        cin >> temp >> k;

        int s = temp.size();
        for(int i = 0; i < s; i++)
            pancakes[i] = temp[i] == '+' ? true : false;

        int flips = 0;
        for(int i = 0; i < s - k + 1; i++)
        {
            if(!pancakes[i])
            {
                for(int j = 0; j < k; j++)
                {
                    pancakes[i + j] = !pancakes[i + j];
                }
                flips++;
            }
        }

        int correct = true;
        for(int i = s - k + 1; i < s; i++)
        {
            if(!pancakes[i])
                correct = false;
        }
        cout << "Case #" << (q + 1) << ": ";
        if(correct)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }


    return 0;
}
