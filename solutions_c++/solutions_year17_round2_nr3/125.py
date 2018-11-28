#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
#define ll long long
#define infini 1000000000000000

using namespace std;

#define entree fin
#define sortie fout

int main()
{
    int nbTests,iTest,nbVilles,iVille,jVille,kVille,nbRequetes,iRequete;
    ifstream fin("C-large.in");
    ofstream fout("Clarge.out");
    sortie<<fixed<<setprecision(7);
    entree>>nbTests;
    for(iTest=0; iTest<nbTests; iTest++)
    {
        entree>>nbVilles>>nbRequetes;
        double dist[nbVilles][nbVilles];
        double vitesse[nbVilles];
        double limite[nbVilles];
        for(iVille=0; iVille<nbVilles; iVille++)
        {
            entree>>limite[iVille]>>vitesse[iVille];
        }
        for(iVille=0; iVille<nbVilles; iVille++)
        {
            for(jVille=0; jVille<nbVilles; jVille++)
            {
                entree>>dist[iVille][jVille];
                if(dist[iVille][jVille]==-1)
                {
                    dist[iVille][jVille]=infini;
                }
            }
            dist[iVille][iVille]=0;
        }
        for(kVille=0; kVille<nbVilles; kVille++)
        {
            for(iVille=0; iVille<nbVilles; iVille++)
            {
                for(jVille=0; jVille<nbVilles; jVille++)
                {
                    dist[iVille][jVille]=min(dist[iVille][jVille],dist[iVille][kVille]+dist[kVille][jVille]);
                }
            }
        }
        for(iVille=0; iVille<nbVilles; iVille++)
        {
            for(jVille=0; jVille<nbVilles; jVille++)
            {
                if(dist[iVille][jVille]>limite[iVille])
                {
                    dist[iVille][jVille]=infini;
                }
                else
                {
                    dist[iVille][jVille]/=vitesse[iVille];
                }
            }
        }
        for(kVille=0; kVille<nbVilles; kVille++)
        {
            for(iVille=0; iVille<nbVilles; iVille++)
            {
                for(jVille=0; jVille<nbVilles; jVille++)
                {
                    dist[iVille][jVille]=min(dist[iVille][jVille],dist[iVille][kVille]+dist[kVille][jVille]);
                }
            }
        }
        sortie<<"Case #"<<iTest+1<<":";
        for(iRequete=0;iRequete<nbRequetes;iRequete++)
        {
            int depart,pin;
            entree>>depart>>pin;
            depart--;
            pin--;
            sortie<<" "<<dist[depart][pin];
        }
        sortie<<endl;
    }
    return 0;
}
