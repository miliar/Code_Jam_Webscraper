#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main(){
    int personnesN;
    int placesN;
    bool controle = true;
    string places="";
    string personnes = "";
    string courant;
    ifstream fichier("C-small-2-attempt3.in", ios::in);
    if(!fichier){
        cout<<"Erreur à l'ouverture du fichier"<<endl;
        return -1;
    }
    ofstream fichier1("test.txt", ios::out | ios::trunc);
    if(fichier1)
    {
        getline(fichier,courant);
        int a = atoi(courant.c_str());
        for(int aze=1;aze<=a;aze++){
            places = "";
            personnes = "";
            controle = true;
            getline(fichier,courant);

            for(int i=0;i<courant.size();i++){
                if(controle){
                    if(courant[i]==' ')
                        controle=false;
                    else
                        places+=courant[i];
                }else{
                    personnes+=courant[i];
                }
            }
            personnesN = atoi(personnes.c_str());
            placesN = atoi(places.c_str());

            fichier1 << "Case #"<<aze<<": ";
            int i = 0;
            while(1){
                if(personnesN<pow(2,i)){
                    break;
                }
                i++;
            }
            int a = (placesN - (personnesN - pow(2,i-1)))/pow(2,i);
            int b = (placesN-personnesN)/pow(2,i);
            fichier1 << a <<" "<< b <<endl;
        }
        fichier.close();
        fichier1.close();
    }
    else
        cout << "Impossible d'ouvrir le fichier !" << endl;

    return 0;
}
