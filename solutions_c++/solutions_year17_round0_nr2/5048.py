#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main(){
    int b=1;
    string courant="";
    string tmp = "";
    ifstream fichier("B-large.in", ios::in);
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
            tmp="";
            getline(fichier,courant);
            fichier1 << "Case #"<<aze<<": ";
            if(courant.size()!=1){
                for(int i = courant.size()-1; i>0; i--){
                    if(courant[i] < courant[i-1]){
                        courant[i-1] -= 1;
                        for(int j=i; j<courant.size(); j++){
                            courant[j]='9';
                        }
                    }
                }
                for(int c=0;c<courant.size();c++){
                    if(courant[c]!='0')
                        tmp += courant[c];
                }
                fichier1 << tmp <<endl;
            }else{
                fichier1 << courant <<endl;
            }
        }

        fichier.close();
        fichier1.close();
    }
    else
        cout << "Impossible d'ouvrir le fichier !" << endl;

    return 0;
}
