#include <bits/stdc++.h>

using namespace std;
char Rouf[6]={'R', 'O', 'Y', 'G', 'B', 'V'};
int maxtab(int tab[],char b)
{
    int x=-1,pos=0;
    for (int i=0;i<6;i++)
    {
        if (tab[i]>x && Rouf[i]!=b)
        {
            x=tab[i];
            pos=i;
        }
    }
    return pos;
}

int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,cs=0;
    cin >> t;
    while (t--)
    {
        cs++;
        int n,T[7];
        cin >> n;
        bool ok=false;
        for (int i=0;i<6;i++)
        {
            cin >> T[i];
            if (T[i]>(n/2))
                ok=true;
        }
        cout <<"Case #"<<cs;
        if (n==1)
        {
            int j=0;
            while (T[j]==0)
            {
                j++;
            }
            cout << ": "<<Rouf[j]<<"\n";
            continue;
        }
        if (ok)
        {
            cout<<": IMPOSSIBLE\n";
            continue;
        }
        cout << ": ";
        int j=0;
        while (T[j]==0)
            j++;
        cout << Rouf[j];
        char pred=Rouf[j];
        T[j]--;
        n--;
        while (n>0)
        {
            j=maxtab(T,pred);
            cout << Rouf[j];
            pred=Rouf[j];
            n--;
            T[j]--;
        }
        cout << "\n";
    }
    return 0;
}
