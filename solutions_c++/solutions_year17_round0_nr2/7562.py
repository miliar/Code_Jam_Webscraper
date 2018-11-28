#include <iostream>
#include <string.h>

using namespace std;

void calc(char N[])
{
    int len;
    int i, j;

    int ind = -1;

    len = strlen(N);

for (int q=0 ; q<18 ; q++) // just repeat thrice...
{
    for (i=0 ; i<(len-1) ; i++)
    {
        if (N[i] > N[i+1])
        {
            ind = i;
            break;
        }
    }

    if (ind>=0)
    {
        --N[i];

        for (i=(ind+1) ; i<len ; i++)
            N[i] = '9';
    }

}

    if (N[0]=='0')
    {
        for (j=0 ; j<len ; j++)
        {
            N[j] = N[j+1];
        }
    }

    cout << N << '\n';
}

int main()
{
    int T, x;

    char last[21];

    cin >> T;

    for (x=0 ; x<T ; x++)
    {
        cin >> last;
        cout << "Case #" << x+1 <<": ";
        calc(last);
    }

    return 0;
}
