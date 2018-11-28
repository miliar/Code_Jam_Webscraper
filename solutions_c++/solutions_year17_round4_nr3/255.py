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

char terrain[52][52];
int acces[52][52];

vector<int> laser(int ligne,int colonne,bool horizontal)
{
    vector<int> reponse;
    bool quitte;
    int lLaser,cLaser,direction;//8624
    lLaser=ligne;
    cLaser=colonne;
    if(horizontal)
    {
        direction=6;
    }
    else
    {
        direction=8;
    }
    quitte=false;
    while(!quitte)
    {
        switch(direction)
        {
        case 8:
            lLaser--;
            break;
        case 6:
            cLaser++;
            break;
        case 4:
            cLaser--;
            break;
        case 2:
            lLaser++;
            break;
        }
        reponse.push_back(lLaser);
        reponse.push_back(cLaser);
        switch(terrain[lLaser][cLaser])
        {
        case '.':
            break;
        case '\\':
            if(direction>4)
                direction-=4;
            else
                direction+=4;
            break;
        case '/':
            if(direction%4==0)
                direction-=2;
            else
                direction+=2;
            break;
        default:
            quitte=true;
            break;
        }
    }
    lLaser=ligne;
    cLaser=colonne;
    if(horizontal)
    {
        direction=4;
    }
    else
    {
        direction=2;
    }
    quitte=false;
    while(!quitte)
    {
        switch(direction)
        {
        case 8:
            lLaser--;
            break;
        case 6:
            cLaser++;
            break;
        case 4:
            cLaser--;
            break;
        case 2:
            lLaser++;
            break;
        }
        reponse.push_back(lLaser);
        reponse.push_back(cLaser);
        switch(terrain[lLaser][cLaser])
        {
        case '.':
            break;
        case '\\':
            if(direction>4)
                direction-=4;
            else
                direction+=4;
            break;
        case '/':
            if(direction%4==0)
                direction-=2;
            else
                direction+=2;
            break;
        default:
            quitte=true;
            break;
        }
    }
    return reponse;
}

int main()
{
    int nbTests,iTest,nbLignes,nbColonnes,iLigne,iColonne;
    ifstream fin("C-small-attempt0.in");
    ofstream fout("Csmall.out");
    //sortie<<fixed<<setprecision(7);
    entree>>nbTests;
    for(iTest=0; iTest<nbTests; iTest++)
    {
        entree>>nbLignes>>nbColonnes;
        nbColonnes+=2;
        nbLignes+=2;
        bool possible(true);
        char c;
        for(iLigne=0; iLigne<nbLignes; iLigne++)
        {
            for(iColonne=0; iColonne<nbColonnes; iColonne++)
            {
                if(iLigne==0||iLigne==nbLignes-1||iColonne==0||iColonne==nbColonnes-1)
                {
                    c='#';
                }
                else
                {
                    entree>>c;
                }
                if(c=='|'||c=='-')
                {
                    c='*';
                }
                terrain[iLigne][iColonne]=c;
                acces[iLigne][iColonne]=0;
            }
        }
        sortie<<"Case #"<<iTest+1<<": ";
        vector<int> casesAtteignables;
        for(iLigne=0; iLigne<nbLignes; iLigne++)
        {
            for(iColonne=0; iColonne<nbColonnes; iColonne++)
            {
                if(terrain[iLigne][iColonne]=='*')
                {
                    bool bonHor(true),bonVer(true);
                    casesAtteignables=laser(iLigne,iColonne,true);
                    for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                    {
                        c=terrain[casesAtteignables[i]][casesAtteignables[i+1]];
                        if(c=='*'||c=='|'||c=='-')
                        {
                            bonHor=false;
                        }
                    }
                    casesAtteignables=laser(iLigne,iColonne,false);
                    for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                    {
                        c=terrain[casesAtteignables[i]][casesAtteignables[i+1]];
                        if(c=='*'||c=='|'||c=='-')
                        {
                            bonVer=false;
                        }
                    }
                    if(!bonHor)
                    {
                        if(!bonVer)
                        {
                            sortie<<"IMPOSSIBLE\n";
                            possible=false;
                            break;
                            iLigne=nbLignes;
                        }
                        else
                        {
                            terrain[iLigne][iColonne]='|';
                        }
                    }
                    else if(!bonVer)
                    {
                        terrain[iLigne][iColonne]='-';
                    }
                }
            }
        }
        //Plus de destruction possible
        if(possible)
        {
            for(iLigne=0; iLigne<nbLignes; iLigne++)
            {
                for(iColonne=0; iColonne<nbColonnes; iColonne++)
                {
                    if(terrain[iLigne][iColonne]=='*'||terrain[iLigne][iColonne]=='-')
                    {
                        casesAtteignables=laser(iLigne,iColonne,true);
                        for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                        {
                            acces[casesAtteignables[i]][casesAtteignables[i+1]]++;
                        }
                    }
                    if(terrain[iLigne][iColonne]=='*'||terrain[iLigne][iColonne]=='|')
                    {
                        casesAtteignables=laser(iLigne,iColonne,false);
                        for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                        {
                            acces[casesAtteignables[i]][casesAtteignables[i+1]]++;
                        }
                    }
                }
            }
            //acces est a jour
            bool resteEtoile(true),changement;
            while(resteEtoile)
            {
                resteEtoile=false;
                changement=false;
                for(iLigne=0; iLigne<nbLignes; iLigne++)
                {
                    for(iColonne=0; iColonne<nbColonnes; iColonne++)
                    {
                        if(terrain[iLigne][iColonne]=='*')
                        {
                            resteEtoile=true;
                            casesAtteignables=laser(iLigne,iColonne,true);
                            for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                            {
                                if(terrain[casesAtteignables[i]][casesAtteignables[i+1]]=='.'&&acces[casesAtteignables[i]][casesAtteignables[i+1]]==1)
                                {
                                    terrain[iLigne][iColonne]='-';
                                    casesAtteignables=laser(iLigne,iColonne,false);
                                    for(int j=0; j<(int)casesAtteignables.size(); j+=2)
                                    {
                                        acces[casesAtteignables[j]][casesAtteignables[j+1]]--;
                                    }
                                    changement=true;
                                    iColonne=nbColonnes;
                                    iLigne=nbLignes;
                                    break;
                                }
                            }
                        }
                        if(terrain[iLigne][iColonne]=='*')
                        {
                            casesAtteignables=laser(iLigne,iColonne,false);
                            for(int i=0; i<(int)casesAtteignables.size(); i+=2)
                            {
                                if(terrain[casesAtteignables[i]][casesAtteignables[i+1]]=='.'&&acces[casesAtteignables[i]][casesAtteignables[i+1]]==1)
                                {
                                    terrain[iLigne][iColonne]='|';
                                    casesAtteignables=laser(iLigne,iColonne,true);
                                    for(int j=0; j<(int)casesAtteignables.size(); j+=2)
                                    {
                                        acces[casesAtteignables[j]][casesAtteignables[j+1]]--;
                                    }
                                    changement=true;
                                    iColonne=nbColonnes;
                                    iLigne=nbLignes;
                                    break;
                                }
                            }
                        }
                    }
                }
                if(!changement)
                {
                    for(iLigne=0; iLigne<nbLignes; iLigne++)
                    {
                        for(iColonne=0; iColonne<nbColonnes; iColonne++)
                        {
                            if(terrain[iLigne][iColonne]=='*')
                            {
                                terrain[iLigne][iColonne]='-';
                                casesAtteignables=laser(iLigne,iColonne,false);
                                for(int j=0; j<(int)casesAtteignables.size(); j+=2)
                                {
                                    acces[casesAtteignables[j]][casesAtteignables[j+1]]--;
                                }
                                changement=true;
                                iColonne=nbColonnes;
                                iLigne=nbLignes;
                                break;
                            }
                        }
                    }
                }
            }
        }
        if(possible)
        {
            for(iLigne=0; iLigne<nbLignes; iLigne++)
            {
                for(iColonne=0; iColonne<nbColonnes; iColonne++)
                {
                    if(terrain[iLigne][iColonne]=='.'&&acces[iLigne][iColonne]==0)
                    {
                        sortie<<"IMPOSSIBLE\n";
                        iLigne=nbLignes;
                        possible=false;
                        break;
                    }
                }
            }
        }
        if(possible)
        {
            sortie<<"POSSIBLE"<<endl;
            for(iLigne=1; iLigne<nbLignes-1; iLigne++)
            {
                for(iColonne=1; iColonne<nbColonnes-1; iColonne++)
                {
                    sortie<<terrain[iLigne][iColonne];
                }
                sortie<<endl;
            }
        }
    }
    return 0;
}
