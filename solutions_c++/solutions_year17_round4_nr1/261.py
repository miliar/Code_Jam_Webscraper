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
    int nbTests,iTest,nbGroupes,taillePaquet,iGroupe,tailleGroupe;
    ifstream fin("A-small-attempt0.in");
    ofstream fout("Asmall.out");
    //sortie<<fixed<<setprecision(7);
    entree>>nbTests;
    for(iTest=0; iTest<nbTests; iTest++)
    {
        entree>>nbGroupes>>taillePaquet;
        int nbTypes[taillePaquet];
        for(iGroupe=0; iGroupe<taillePaquet; iGroupe++)
        {
            nbTypes[iGroupe]=0;
        }
        for(iGroupe=0; iGroupe<nbGroupes; iGroupe++)
        {
            entree>>tailleGroupe;
            nbTypes[tailleGroupe%taillePaquet]++;
        }
        sortie<<"Case #"<<iTest+1<<": ";
        int chocDonne(nbTypes[0]);
        switch(taillePaquet)
        {
        case 2:
            sortie<<nbTypes[0]+(nbTypes[1]+1)/2;
            break;
        case 3:
            while(nbTypes[1]>0&&nbTypes[2]>0)
            {
                nbTypes[1]--;
                nbTypes[2]--;
                chocDonne++;
            }
            chocDonne+=(nbTypes[1]+2)/3;
            chocDonne+=(nbTypes[2]+2)/3;
            sortie<<chocDonne;
            break;
        default:
            while(nbTypes[2]>1)
            {
                chocDonne++;
                nbTypes[2]-=2;
            }
            while(nbTypes[1]>0&&nbTypes[3]>0)
            {
                nbTypes[1]--;
                nbTypes[3]--;
                chocDonne++;
            }
            if(nbTypes[1]>1&&nbTypes[2]>0)
            {
                chocDonne++;
                nbTypes[2]--;
                nbTypes[1]-=2;
            }
            if(nbTypes[3]>1&&nbTypes[2]>0)
            {
                chocDonne++;
                nbTypes[2]--;
                nbTypes[3]-=2;
            }
            chocDonne+=(nbTypes[1]+3)/4;
            chocDonne+=(nbTypes[3]+3)/4;
            sortie<<chocDonne;
            break;
        }
        sortie<<endl;
    }
    return 0;
}
