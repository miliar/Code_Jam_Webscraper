#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <cstddef>

using namespace std;

int main()
{
    //string const FichierEntree;
	//cin >> FichierEntree;
    string const FichierEntree("./B-large.in");
    //string const FichierEntree("./test.txt");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int N, K, J, size;
        string S;
		int nbT;
        Input >> nbT;
        
        for (int i=1; i<=nbT; i++) //nbT
        {
            Input >> S;
            cout<<"S = "<<S<<endl;
            size = S.size();
            /*for (int j=1;j<19;j++)
            {
                //cout<<pow(10,j-1)<<endl;
                if ((K>pow(10,j-1))&&(K<pow(10,j)))
                {
                    size = j;
                }
            }*/
            cout<<"size = "<<size<<endl;
                
            int* nb = new int[size];
            cout<<"nb = ";
            //double test = K;
            for (int j=0;j<size; j++)
            {
                //nb[j]=floor(test*1.0/pow(10,size-1-j));
                //test -= nb[j]*pow(10,size-1-j);
                //cout<<S[j]<<" "<<(int)S[j]-48<<endl;
                nb[j]=(int)S[j]-48;
                cout<<nb[j]<<" ";
            }
            
            cout<<endl;
            
            int check =1;
            int it = 0;
            while (check>0 && it<size)
            {
                check =0;
                for (int j=1;j<size; j++)
                {
                    if (nb[j]<nb[j-1])
                    {
                        check = 1;
                        nb[j-1]-= 1;
                        for (int k=j;k<size;k++)
                            nb[k]=9;
                        cout << "check=1 "<< "nb = "<<nb[0]<<" "<<nb[1]<<" "<<nb[2]<<" "<<nb[3]<<endl;
                    }
                }
                it +=1;
            }
            cout<<"nb = "<<nb[0]<<" "<<nb[1]<<" "<<nb[2]<<" "<<nb[3]<<endl;
            
            Output << "Case #" << i<<": ";
            for (int j=0;j<size;j++)
            {
                if (nb[j]>0)
                    Output<<nb[j];
            }
            Output<<endl;
            
        }
		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}
