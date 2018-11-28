#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

void retourneur(string* liste,int* numFin);
void tourne(int i,int j, string* liste,int planche);

int main()
{
    int tailleFich=101;
    string courant;
    int numFin[tailleFich];
    string liste[tailleFich];
    for(int j=0;j<tailleFich;j++)
    {
        liste[j]="";
    }
    int i=0;

    ifstream fichier("attemp.in", ios::in);
    if(!fichier){
        cout<<"Erreur à l'ouverture du fichier"<<endl;
        return -1;
    }
    string tamp="";
    bool grand=false;
    //remplissage
    while(getline(fichier,courant))
    {
        if(i>0)
        {
            tamp="";
            for(int j=0;j<courant.length();j++)
            {
                if(courant[j]=='+' ||courant[j]=='-')
                {
                    liste[i]=liste[i]+courant[j];
                }
                else if(courant[j]!='+' && courant[j]!='-'&& courant[j]!=' ')
                {
                    tamp=tamp+courant[j];
                }
            }
            numFin[i]=atof(tamp.c_str());

        }
        i++;

    }
    fichier.close();


    retourneur(liste,numFin);



    return 0;
}

void retourneur(string* liste,int* numFin)
{
    bool termine=false;
    bool imp=false;
    string tamp;
    int cpt;
    ofstream fichier("testres.txt", ios::out | ios::trunc);

    if(fichier)
    {
        for(int i=0;i<101;i++)
        {
            cpt=0;
            imp=false;
                for(int j=0;j<liste[i].length();j++)
                {
                    tamp=liste[i];
                    if(tamp[j]=='-')
                    {
                        if(liste[i].length()-j>=numFin[i])
                        {
                            tourne(i,j,liste,numFin[i]);
                            cpt++;
                        }
                        else
                        {
                            imp=true;
                        }

                    }
                }
                if(i>0)
                {
                    if(imp==false)
                    {
                        fichier << "Case #" <<i<<": "<< cpt << endl;
                    }
                    else
                    {
                        fichier << "Case #" <<i<<": IMPOSSIBLE"<<endl;
                    }
                }

            }

        }
        else
                cerr << "Impossible d'ouvrir le fichier !" << endl;
}


void tourne(int i,int j, string* liste,int planche)
{
    for(int k=j;k<j+planche;k++)
    {
        if(liste[i][k]=='-')
        {
            liste[i][k]='+';
        }
        else
        {
            liste[i][k]='-';
        }
    }
}











