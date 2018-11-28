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
    int nbTests,iTest,nbSieges,nbClients,nbTickets,iTicket,iClient,iSiege;
    ifstream fin("B-large.in");
    ofstream fout("Blarge.out");
    //sortie<<fixed<<setprecision(7);
    entree>>nbTests;
    for(iTest=0; iTest<nbTests; iTest++)
    {
        entree>>nbSieges>>nbClients>>nbTickets;
        int place[nbTickets];
        int client[nbTickets];
        int nbReservations[nbClients];
        int nbAvant[nbSieges];
        for(iClient=0;iClient<nbClients;iClient++)
        {
            nbReservations[iClient]=0;
        }
        for(iSiege=0;iSiege<nbSieges;iSiege++)
        {
            nbAvant[iSiege]=0;
        }
        for(iTicket=0;iTicket<nbTickets;iTicket++)
        {
            entree>>place[iTicket]>>client[iTicket];
            place[iTicket]--;
            client[iTicket]--;
            nbReservations[client[iTicket]]++;
            nbAvant[place[iTicket]]++;
        }
        int nbRides(0),avantTotal(0),deplacements(0);
        for(iClient=0;iClient<nbClients;iClient++)
        {
            nbRides=max(nbRides,nbReservations[iClient]);
        }
        for(iSiege=0;iSiege<nbSieges;iSiege++)
        {
            avantTotal+=nbAvant[iSiege];
            nbRides=max(nbRides,(avantTotal+iSiege)/(iSiege+1));
        }
        for(iSiege=0;iSiege<nbSieges;iSiege++)
        {
            if(nbAvant[iSiege]>nbRides)
            {
                deplacements+=(nbAvant[iSiege]-nbRides);
            }
        }
        sortie<<"Case #"<<iTest+1<<": "<<nbRides<<" "<<deplacements;
        sortie<<endl;
    }
    return 0;
}
