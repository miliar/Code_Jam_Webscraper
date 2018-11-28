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
    int nbTests,iTest,iCheval,nbChevaux,depart,dist;
    double tMax,vitesse;
    ifstream fin("A-large.in");
    ofstream fout("Alarge.out");
    sortie<<setprecision(7)<<fixed;
    entree>>nbTests;
    for(iTest=0;iTest<nbTests;iTest++)
    {
        entree>>dist>>nbChevaux;
        tMax=0;
        for(iCheval=0;iCheval<nbChevaux;iCheval++)
        {
            entree>>depart>>vitesse;
            tMax=max(tMax,(double)(dist-depart)/vitesse);
        }
        sortie<<"Case #"<<iTest+1<<": ";
        sortie<<dist/tMax<<endl;
    }
    return 0;
}
