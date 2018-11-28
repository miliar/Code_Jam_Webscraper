#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
#define ll long long

using namespace std;

#define entree fin
#define sortie fout

int main()
{
    int nbTests,iTest,nbLicornes,iLicorne,r,o,y,g,b,v,dernier;
    ifstream fin("B-large.in");
    ofstream fout("Blarge.out");
    entree>>nbTests;
    for(iTest=0; iTest<nbTests; iTest++)
    {
        entree>>nbLicornes;
        entree>>r>>o>>y>>g>>b>>v;
        sortie<<"Case #"<<iTest+1<<": ";
        r-=g;
        y-=v;
        b-=o;
        nbLicornes-=(2*(v+g+o));
        if(2*r>nbLicornes||2*y>nbLicornes||2*b>nbLicornes||(r<=0&&g!=0&&(r!=0||y+b+r>0))||(y<=0&&v!=0&&(y!=0||y+b+r>0))||(b<=0&&o!=0&&(b!=0||y+b+r>0)))
        {
            sortie<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            if(r==0&&b==0&&y==0)
            {
                if((o>0&&(v>0||g>0))||(v>0&&g>0))
                    sortie<<"IMPOSSIBLE"<<endl;
                else
                {
                    string s;
                    if(o>0)
                        s="BO";
                    if(g>0)
                        s="RG";
                    if(v>0)
                        s="YV";
                    for(int i=0; i<o+g+v; i++)
                    {
                        sortie<<s;
                    }
                    sortie<<endl;
                }
            }
            else{
            if(r>=y&&r>=b)
                dernier=0;
            if(y>=r&&y>=b)
                dernier=2;
            if(b>=r&&b>=y)
                dernier=4;
            int ini=dernier;
            for(int i=0; i<nbLicornes; i++)
            {
                switch(dernier)
                {
                case 0:
                    if(y>b||(y==b&&ini==4))
                    {
                        dernier=2;
                        y--;
                        sortie<<'Y';
                        while(v!=0)
                        {
                            sortie<<"VY";
                            v--;
                        }
                    }
                    else
                    {
                        dernier=4;
                        b--;
                        sortie<<'B';
                        while(o!=0)
                        {
                            sortie<<"OB";
                            o--;
                        }
                    }
                    break;
                case 2:
                    if(r>b||(r==b&&ini==4))
                    {
                        dernier=0;
                        r--;
                        sortie<<'R';
                        while(g!=0)
                        {
                            sortie<<"GR";
                            g--;
                        }
                    }
                    else
                    {
                        dernier=4;
                        b--;
                        sortie<<'B';
                        while(o!=0)
                        {
                            sortie<<"OB";
                            o--;
                        }
                    }
                    break;
                case 4:
                    if(r>y||(r==y&&ini==2))
                    {
                        dernier=0;
                        r--;
                        sortie<<'R';
                        while(g!=0)
                        {
                            sortie<<"GR";
                            g--;
                        }
                    }
                    else
                    {
                        dernier=2;
                        y--;
                        sortie<<'Y';
                        while(v!=0)
                        {
                            sortie<<"VY";
                            v--;
                        }
                    }
                    break;
                }
            }
            sortie<<endl;
        }}
    }
    return 0;
}
