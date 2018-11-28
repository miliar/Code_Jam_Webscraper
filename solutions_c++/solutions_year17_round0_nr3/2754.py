#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    ifstream f("bathroom.in");
    ofstream g("bathroom.out");

    int t;
    f>>t;

    long long n, e, eddig;

    struct x
    {
        long long sz, arany;
    };

    x szamok[3];
    for(int i=1; i<=t; i++)
    {
        f>>n>>e;
        g<<"Case #"<<i<<": ";
        szamok[1].sz=n;
        szamok[1].arany=1;
        szamok[2].sz=0;
        szamok[2].arany=0;
        eddig=1;
        long long szint=1;
        while(eddig<e)
        {
            if(szamok[2].arany==0)
            {
                if(szamok[1].sz%2==1)
                {
                    szamok[1].sz/=2;
                    szamok[1].arany*=2;
                }
                else
                {
                    szamok[1].sz=szamok[1].sz/2-1;
                    szamok[2].sz=szamok[1].sz+1;
                    szamok[2].arany=szamok[1].arany;
                }
            }
            else
            {
                if(szamok[1].sz%2==0)
                {
                    szamok[1].sz=szamok[1].sz/2-1;
                    szamok[2].arany*=2;
                    szamok[2].arany+=szamok[1].arany;
                    szamok[2].sz=szamok[1].sz+1;
                }
                else
                {
                    szamok[1].sz/=2;
                    szamok[1].arany=szamok[1].arany*2+szamok[2].arany;
                    szamok[2].sz=szamok[1].sz+1;
                }
            }

            szint*=2;
            if(eddig==0) eddig=1;
            else eddig+=szint;
        }

        if(e-(eddig-szint)<=szamok[2].arany)
        {
            if(szamok[2].sz%2==0)
            {
                g<<szamok[2].sz/2<<" "<<szamok[2].sz/2-1<<endl;
            }
            else g<<szamok[2].sz/2<<" "<<szamok[2].sz/2<<endl;
        }
        else
        {
            if(szamok[1].sz%2==0)
            {
                g<<szamok[1].sz/2<<" "<<szamok[1].sz/2-1<<endl;
            }
            else g<<szamok[1].sz/2<<" "<<szamok[1].sz/2<<endl;
        }

    }
    return 0;
}
