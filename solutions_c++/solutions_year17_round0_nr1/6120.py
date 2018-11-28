#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-soln.out","w",stdout);
    int trials;
    cin >> trials;
    cin.ignore();
    int initrials = trials + 1;
    while (trials > 0)
    {
        string pancakes;
        int counter = 0;
        int spatula;
        char input;
        bool done = false;
        input = getchar();
        while (!(input == ' '))
        {
            pancakes += input;
            input = getchar();
        }
        cin >> spatula;
        for(int i=0; i<=pancakes.size()-spatula; i++)
        {
            if(pancakes[i] == '-')
            {
                pancakes[i] = '+';
                int index = i+1;
                while (index <= i+spatula-1)
                {
                    if (pancakes[index] == '+')
                        pancakes[index] = '-';
                    else
                        pancakes[index] = '+';
                    ++index;
                }
                ++counter;
            }
        }
        for(int i=pancakes.size()-spatula; i<=pancakes.size()-1; i++)
        {
            if (pancakes[i] == '-')
            {
                cout << "Case #" << initrials - trials << ": " << "IMPOSSIBLE" << endl;
                done = true;
                break;
            }
        }
        if (done == false)
            cout << "Case #" << initrials - trials << ": " << counter << endl;
        --trials;
    }
    return 0;
}
