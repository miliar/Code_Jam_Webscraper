#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
#define ll long long

using namespace std;

#define entree fin
#define sortie fout

int main()
{
    ll nbStalls,nbGens,nbTests,nbPlaces,lo;
    ll lenInter[4];//Les 4 longueurs par ordre croissant
    ll places[4];//Le nombre de places par type
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    entree>>nbTests;
    for(ll iTest=0;iTest<nbTests;iTest++)
    {
        entree>>nbStalls>>nbGens;
        lenInter[0]=nbStalls/2-1;
        lenInter[1]=(nbStalls/2);
        lenInter[2]=nbStalls;
        lenInter[3]=nbStalls+1;
        places[0]=0;
        places[1]=0;
        places[2]=1;
        places[3]=0;
        while(nbGens>0)
        {
            if(places[3]==0&&(places[2]==0||lenInter[2]==0))
            {
                places[2]=places[0];
                places[3]=places[1];
                places[0]=0;
                places[1]=0;
                lenInter[2]=lenInter[0];
                lenInter[3]=lenInter[1];
                lenInter[0]=(lenInter[2]-1)/2;
                lenInter[1]=(lenInter[2]+1)/2;
            }
            if(places[3]!=0)
            {
                nbPlaces=places[3];
                lo=lenInter[3];
                places[3]=0;
            }
            else
            {
                nbPlaces=places[2];
                lo=lenInter[2];
                places[2]=0;
            }
            if(nbGens<=nbPlaces)
            {
                sortie<<"Case #"<<iTest+1<<": "<<lo/2<<" "<<(lo-1)/2<<endl;
                nbGens=0;
            }
            else
            {
                nbGens-=nbPlaces;
                if(lenInter[0]==(lo-1)/2)
                {
                    places[0]+=nbPlaces;
                }
                else
                {
                    places[1]+=nbPlaces;
                }
                if(lenInter[0]==lo/2)
                {
                    places[0]+=nbPlaces;
                }
                else
                {
                    places[1]+=nbPlaces;
                }
            }
        }
    }
    return 0;
}
