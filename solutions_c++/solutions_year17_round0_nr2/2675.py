#include <iostream>
#include <fstream>


using namespace std;

void fordit(int a[], int ahossz)
{
    for(int i=1; i<=ahossz/2; i++) swap(a[i], a[ahossz-i+1]);
}

int main()
{
    ifstream f("tidy.in");
    ofstream g("tidy.out");

    int t;
    f>>t;

    long long  n;
    int a[20];
    int ahossz;

    int akt;
    int e;
    bool talalt;
    for(int k=1; k<=t; k++)
    {
        f>>n;
        g<<"Case #"<<k<<": ";
        if(n<=9) g<<n<<endl;
        else
        {
            akt=1;
            ahossz=0;
            while(n>0)
            {
                ahossz++;
                a[akt]=n%10;
                n/=10;
                akt++;
            }
            fordit(a, ahossz);


            talalt=false;
            for(int i=1; i<=ahossz-1 and !talalt; i++)
            {
                if(a[i]>a[i+1])
                {
                    e=i;
                    talalt=true;
                }
            }

            if(!talalt)
            {
                for(int i=1; i<=ahossz; i++) g<<a[i];
                g<<endl;
            }
            else
            {
                if(a[e]==1)
                {
                    for(int i=1; i<=ahossz-1; i++) g<<'9';
                    g<<endl;
                }
                else
                {
                    while(a[e]-1<a[e-1] and e>=2) e--;
                    if(e==1)
                    {
                        if(a[e]==1)
                        {
                            for(int i=1; i<=ahossz-1; i++) g<<'9';
                            g<<endl;
                        }
                        else
                        {
                            g<<a[e]-1;
                            for(int i=1; i<=ahossz-1; i++) g<<'9';
                            g<<endl;
                        }
                    }
                    else
                    {
                        a[e]--;
                        for(int i=e+1; i<=ahossz; i++)
                        {
                            a[i]=9;
                        }
                        for(int i=1; i<=ahossz; i++) g<<a[i];
                        g<<endl;
                    }
                }
            }
        }

    }
    return 0;
}
