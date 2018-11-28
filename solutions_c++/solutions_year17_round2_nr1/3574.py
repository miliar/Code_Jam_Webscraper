#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
using namespace std;

int main(){
    string courant;
    string distTot,nbConcu,distConcu,vitesseConcu;
    bool controle;
    int nbConcuN;
    double distTotN,distConcuN,vitesseConcuN;
    double tempsMin=-1;
    ifstream fichier("A-large.in", ios::in);
    if(!fichier){
        cout<<"Erreur à l'ouverture du fichier"<<endl;
        return -1;
    }
    FILE* fichier1 = fopen("test.txt", "w");
    if(fichier1)
    {
        getline(fichier,courant);
        int a = atoi(courant.c_str());
        for(int aze=1;aze<=a;aze++){
            getline(fichier,courant);
            distTot="";
            nbConcu="";
            controle = true;
            for(int i=0;i<courant.size();i++){
                if(controle){
                    if(courant[i]==' ')
                        controle=false;
                    else
                        distTot+=courant[i];
                }else{
                    nbConcu+=courant[i];
                }
            }
            distTotN = atof(distTot.c_str());
            nbConcuN = atoi(nbConcu.c_str());
            tempsMin=-1;
            for(int i=0;i<nbConcuN;i++){
                getline(fichier,courant);
                controle = true;
                distConcu="";
                vitesseConcu="";
                for(int j=0;j<courant.size();j++){
                    if(controle){
                        if(courant[j]==' ')
                            controle=false;
                        else
                            distConcu+=courant[j];
                    }else{
                        vitesseConcu+=courant[j];
                    }
                }
                distConcuN = atof(distConcu.c_str());
                vitesseConcuN = atof(vitesseConcu.c_str());
                if(tempsMin < ((distTotN-distConcuN)/vitesseConcuN))
                    tempsMin = ((distTotN-distConcuN)/vitesseConcuN);
            }
            fprintf(fichier1, "Case #%d: %.6f\n", aze,(distTotN/tempsMin));
        }
        fichier.close();
        fclose(fichier1);
    }
    else
        cout << "Impossible d'ouvrir le fichier !" << endl;

    return 0;
}

