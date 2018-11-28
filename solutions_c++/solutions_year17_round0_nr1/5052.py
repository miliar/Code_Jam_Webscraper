#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main(){
    string courant = "";
    string symb = "";
    string plage = "";
    bool controle = false;
    int i=0;
    int j=0;
    int k=0;
    int taillePlage;
    ifstream fichier("A-large.in", ios::in);
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
            symb="";
            plage="";
            getline(fichier,courant);
            for(int b=0;b<courant.size();b++){
                if(courant[b]=='-' || courant[b]=='+'){
                    symb+=courant[b];
                }else if(courant[b]!=' '){
                    plage+=courant[b];
                }
            }
            taillePlage = atoi(plage.c_str());;

            fichier1 << "Case #"<<aze<<": ";
            i=0;k=0;
            controle=false;
            while(i!=symb.size()){
                if(symb[i] == '-'){
                    if(symb.size()-i<taillePlage){
                        fichier1<<"IMPOSSIBLE"<<endl;
                        controle = true;
                        break;
                    }
                    for(int j=0;j<taillePlage;j++){
                        (symb[i+j]=='-')?symb[i+j]='+':symb[i+j]='-';
                    }
                    k++;
                }
                i++;
            }
            if(!controle){
                fichier1<<k<<endl;
            }
        }

        fichier.close();
        fichier1.close();
    }
    else
        cout << "Impossible d'ouvrir le fichier !" << endl;

    return 0;
}
