#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

int t;

char n[100];

int poz=-1;

bool isOrdered()
{
    int i=0;
    while(n[i+1])
    {
        if(n[i]>n[i+1])
        {
            poz=i;
            return false;
        }
        i++;
    }
    return true;
}

void getPrev()
{
    int i=strlen(n)-1;

    if(n[i]=='0')
    {
        if(n[i-1]=='1')
        {
            n[i--]=NULL;
            while(n[i]=='1')
            {
                n[i]='9';
                i--;
            }
            n[i]--;
        }
        else
        {
            n[i]='9';
            n[i-1]--;
        }

    }
    else
    {
        n[i]--;
    }
}

void fill9()
{
    while(n[poz])
    {
        n[poz]='9';
        poz++;
    }

}

void solve2()
{
    while(!isOrdered())
    {
        getPrev();
    }
}

void solve()
{
    if(!isOrdered())
    {
        if(n[poz]!='1')
        {
            n[poz]--;
            poz++;
        }
        else
        {
            n[strlen(n)-1]=NULL;
            while(poz>=1 && n[poz-1]=='1')
            {
                poz--;
            }
        }

        fill9();
    }
}

void display(int t, int fin)
{
    cout<<"Case #"<<t<<": ";
    cout<<n;
    if(t!=fin)
        cout<<'\n';
}

void read()
{
    fin>>t;
    for(int i=1; i<=t; i++)
    {
        cin.get();
        cin.get(n,100);
        solve();
        display(i,t);
    }
}

int main()
{
    read();
    return 0;
}
