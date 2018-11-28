#include <iostream>

using namespace std;

double tim(int K, int S, int D)
{
    double tim;

    tim = (double)(D-K)/S;
    return tim;
}

void calc(int D, int N)
{
    int i, j;
    int Klist[1010]; //
    int Slist[1010]; //
    double tlist[1010]; //

    for (i=0 ; i<N ; i++)
    {
        cin >> Klist[i];
        cin >> Slist[i];

        tlist[i] = tim(Klist[i],Slist[i],D);
    }

    double maxtime;
    maxtime = 0;

    for (i=0 ; i<N ; i++)
    {
        if (tlist[i]>maxtime)
            maxtime=tlist[i];
    }
    cout.precision(15);
    cout << (D/maxtime);
}

int main()
{
    int T, x;
    cin >> T;

    int D, N;

    for (x=0 ; x<T ; x++)
    {
        cin >> D;
        cin >> N;
        cout << "Case #" << x+1 <<": ";
        calc(D, N);
        cout << endl;
    }
    return 0;
}
