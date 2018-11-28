#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;


void reduit(string* nbr);

int main()
{
    int tailleFich=101;
    string nbr[tailleFich];
    string courant;
    int i=0;

    ifstream fichier("attemp.in", ios::in);
    if(!fichier)
    {
        cout<<"Erreur à l'ouverture du fichier"<<endl;
        return -1;
    }
    //remplissage
    while(getline(fichier,courant))
    {
        if(i>0)
        {
            for(int j=0;j<courant.length();j++)
            {
                nbr[i]=nbr[i]+courant[j];
            }

        }
        i++;

    }
    fichier.close();

    reduit(nbr);
    return 0;
}


void reduit(string* nbr)
{
    string tamp;
    int tampInt;
    string tampS;
    int tampIntS;
    string res;
    bool pareil=true;

    ofstream fichier("testres.txt", ios::out | ios::trunc);

    if(fichier)
    {
        for(int i=0;i<101;i++)
        {
            pareil=true;
            for (int j=0;j<nbr[i].length();j++)
            {
                //if(nbr[i][j])
                if(j+1!=nbr[i].length())
                {
                    tamp=nbr[i][j];
                    tampInt=atoi(tamp.c_str());
                    tampS=nbr[i][j+1];
                    tampIntS=atoi(tampS.c_str());
                    //cout<<tamp<<"   "<<atoi(tamp.c_str())<<endl;
                    if(tamp>tampS && pareil==true)
                    {

                        pareil=false;
                        res="";
                        if(tampInt==1 && tampIntS==0)
                        {
                            for(int k=0;k<j;k++)
                            {
                                res=res+nbr[i][k];
                            }
                            res=res+'9';
                            for(int k=j+2;k<nbr[i].length();k++)
                            {
                                res=res+'9';
                            }
                        }
                        else
                        {
                            if(j-1>=0)
                            {
                                if(nbr[i][j-1]==nbr[i][j])
                                {
                                    for(int k=0;k<j-1;k++)
                                    {
                                        res=res+nbr[i][k];
                                    }
                                    tamp=nbr[i][j-1];
                                    tampInt=atoi(tamp.c_str());
                                    tampInt--;
                                    ostringstream convert;
                                    convert<<tampInt;
                                    res=res+convert.str();
                                    for(int k=j;k<nbr[i].length();k++)
                                    {
                                        res=res+'9';
                                    }
                                }
                                else
                                {
                                    for(int k=0;k<j;k++)
                                    {
                                        res=res+nbr[i][k];
                                    }
                                    tampInt--;
                                    ostringstream convert;
                                    convert<<tampInt;
                                    res=res+convert.str();
                                    for(int k=j+1;k<nbr[i].length();k++)
                                    {
                                        res=res+'9';
                                    }
                                }
                            }
                            else
                            {
                                for(int k=0;k<j;k++)
                                {
                                    res=res+nbr[i][k];
                                }
                                tampInt--;
                                ostringstream convert;
                                convert<<tampInt;
                                res=res+convert.str();
                                for(int k=j+1;k<nbr[i].length();k++)
                                {
                                    res=res+'9';
                                }
                            }
                        }
                    }
                }


            }
            if(pareil==true)
            {
                res=nbr[i];
            }
            if(i>0)
            {
                fichier << "Case #" <<i<<": "<< res << endl;
            }

        }
    }
    else
                cerr << "Impossible d'ouvrir le fichier !" << endl;
}





