#include <iostream>
#include <fstream>
#include <cstring>


using namespace std;

int main()
{
    ifstream f("pancake.in");
    ofstream g("pancake.out");

    int t;
    f>>t;

    int k;
    string s;

    struct x
    {
        int ert, hanyszor;
    };

    int hossz, db;
    bool jo;
    for(int i=1; i<=t; i++)
    {
        f>>s>>k;
        hossz=s.length();
        x cake[hossz+1];
        db=0;

        g<<"Case #"<<i<<": ";

        for(int j=0; j<=hossz-1; j++)
        {
            if(s[j]=='-') cake[j+1].ert=0;
            else cake[j+1].ert=1;
            cake[j+1].hanyszor=0;
        }

        for(int j=1; j<=hossz-k+1; j++)
        {
            if(cake[j].ert==cake[j].hanyszor%2)
            {
                db++;
                for(int t=j; t<=j+k-1; t++)
                {
                    cake[t].hanyszor++;
                }
            }
        }

        jo=true;

        for(int j=hossz-k+2; j<=hossz and jo; j++)
        {
            if(cake[j].ert==cake[j].hanyszor%2) jo=false;
        }
        if(jo) g<<db<<endl;
        else g<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
