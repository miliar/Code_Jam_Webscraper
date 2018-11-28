#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;



void calc(char S[], int k)
{
    int i;
    int j;

    int counter = 0;

    int len;
    len = strlen(S);

    int A1[1500];

    for (i=0 ; i<len ; i++) // convert to 1/-1
    {
        switch (S[i])
        {
        case '-':
            A1[i] = -1;
            break;
        case '+':
            A1[i] = 1;
            break;
        }

    }

    for (i=0 ; i<=(len-k) ; i++)
    {
        if (A1[i]==-1)
        {
            for (j=i ; j<(i+k) ; j++)
            {
                A1[j] *= -1;
            }
            ++counter;
        }
    }

    int flag = 0;
    for (i=0 ; i<len ; i++)
    {
        if (A1[i] == -1)
        {
            flag = 1;
        }
    }

    if (flag==1)
        cout << "IMPOSSIBLE\n";
    else
        cout << counter << '\n';

}

int main()
{
    int T;
    cin >> T;
    int x;

    char str[1500];
    int flipper;

    for (x=0 ; x<T ; x++)
    {
        cin >> str;
        cin >> flipper;
        cout << "Case #" << x+1 <<": ";
        calc(str, flipper);
    }
    return 0;
}
