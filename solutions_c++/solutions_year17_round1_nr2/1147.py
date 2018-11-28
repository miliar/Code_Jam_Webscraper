#include <iostream>
#include <fstream>
using namespace std;

struct s
{
    int minim, maxim;
    bool volt;
};

int main()
{
    ifstream f("kits.in");
    ofstream g("kits.out");

    int t;
    f>>t;
    int term, cs;

    s lehet[51][51];
    int kell[51];
    int db, ennyi;

    for(int p=1; p<=t; p++)
    {
        f>>term>>cs;
        for(int i=1; i<=term; i++)
        {
            f>>kell[i];
        }

        //szamlalas
        int maximum=0;
        for(int i=1; i<=term; i++)
        {
            for(int j=1; j<=cs; j++)
            {
                f>>db;
                lehet[i][j].volt=false;
                ennyi=1;
                while(!(ennyi*kell[i]*9/10<=db and ennyi*kell[i]*11/10>=db) and ennyi*kell[i]*9/10<=db) ennyi++;
                if(ennyi*kell[i]*9/10<=db and ennyi*kell[i]*11/10>=db)
                {
                    lehet[i][j].minim=ennyi;
                    while(ennyi*kell[i]*9/10<=db and ennyi*kell[i]*11/10>=db) ennyi++;
                    lehet[i][j].maxim=ennyi-1;
                    if(lehet[i][j].maxim>maximum) maximum=lehet[i][j].maxim;
                }
                else
                {
                    lehet[i][j].minim=-1;
                    lehet[i][j].maxim=-1;
                }

            }
        }
        cout<<"Case "<<p<<endl;
        for(int i=1; i<=term; i++)
        {
            for(int j=1; j<=cs; j++)
            {
                cout<<"minim="<<lehet[i][j].minim<<" maxim="<<lehet[i][j].maxim<<"   ";
            }
            cout<<endl;
        }

        //kereses
        bool megvan;
        int ered=0;
        int keresek;
        int ezek[51];
        bool talaltam;

        /*for(int j=1; j<=cs; j++)
        {
            if(lehet[1][j].minim!=-1)
            {
                megvan=false;
                for(int k=lehet[1][j].minim; k<=lehet[1][j].maxim; k++)
                {
                    keresek=k;
                    for(int i=2; i<=term and talaltam; i++)
                    {
                        talaltam=false;
                        for(int l=1; l<=cs; l++)
                        {
                            if(lehet[i][l].minim<=keresek and keresek<=lehet[i][l].maxim)
                            {
                                ezek[i]=l;
                                lehet[i][l].volt=true;
                                talaltam=true;
                            }
                        }
                    }
                    if(talaltam) megvan=true;
                }
            }
        }*/

        int kesz=0;
        int akt=1;
        int valasztottam[51][51]={0};
        int legalabb=50;
        int esorban;
        while(kesz<=cs and akt<=maximum)
        {
            legalabb=50;
            for(int i=1; i<=term and legalabb>0; i++)
            {
                int esorban=0;
                for(int j=1; j<=cs; j++)
                {
                    if(lehet[i][j].minim<=akt and lehet[i][j].maxim>=akt and !lehet[i][j].volt)
                    {
                        valasztottam[i][++esorban]=j;
                    }
                }
                if(esorban<=legalabb) legalabb=esorban;
            }
            kesz+=legalabb;
            for(int i=1; i<=term; i++)
            {
                for(int j=1; j<=legalabb; j++) lehet[i][valasztottam[i][j]].volt=true;
            }
            akt++;
        }
        g<<"case #"<<p<<": "<<kesz<<endl;


    }
    return 0;
}
