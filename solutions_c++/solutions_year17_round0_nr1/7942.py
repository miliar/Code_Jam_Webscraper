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
    string const FichierEntree("./A-large.in");
    //string const FichierEntree("./test.txt");
    string const FichierSortie("./output.txt");
	ifstream Input(FichierEntree.c_str());
	ofstream Output;
	Output.open(FichierSortie.c_str());//, ios::app);

	if(Input)  //On teste si tout est OK
	{
		int N, K, J;

		int nbT;
        Input >> nbT;
        
        for (int i=1; i<=nbT; i++)
        {
            string S = "";
            Input >> S;
            cout<<"S = "<<S<<endl;
            Input >> K;
            cout<<"K = "<<K<<endl;
            
            int size = S.size();
            
            cout<<"pancakes = ";
            int* pancakes = new int[size];
            for (int j=0;j<size; j++)
            {
                char plus = '+';
                char test = S[j];
                if (test==plus)
                    pancakes[j]=1;
                else
                    pancakes[j]=0;
                cout<<pancakes[j]<<" ";
            }
            cout<<endl;
            
            int Sum =0;
            for (int j=0;j<size; j++)
            {
                Sum +=pancakes[j];
            }
            int test = Sum %K;
            
            
            int pos = S.find_first_not_of("+");
            //S.replace(pos,K,)
            int it = 0;
            
            if (pos < size-K+1)
            {
                for (int j=0;j<size-K+1; j++)
                {
                    if (pancakes[j]==0)
                    {
                        it += 1;
                        for (int k=0;k<K;k++)
                        {
                            pancakes[j+k]+=1;
                            pancakes[j+k] = pancakes[j+k] % 2;
                        }
                        cout<<"pancakes = ";
                        for (int j1=0;j1<size;j1++)
                            cout<<pancakes[j1]<<" ";
                        cout<<endl;
                    }
                }
            }
            else
            {
                for (int j=size-1;j>K-1; j--)
                {
                    if (pancakes[j]==0)
                    {
                        it += 1;
                        for (int k=0;k<K;k++)
                        {
                            pancakes[j-k]+=1;
                            pancakes[j-k] = pancakes[j-k] % 2;
                        }
                        cout<<"pancakes = ";
                        for (int j1=0;j1<size;j1++)
                            cout<<pancakes[j1]<<" ";
                        cout<<endl;
                    }
                }

            }
            
            Sum =0;
            for (int j=0;j<size; j++)
            {
                Sum +=pancakes[j];
            }
            
            if (Sum == size)
                Output << "Case #" << i<<": "<<it<<endl;
            else
                Output << "Case #" << i<<": "<<"IMPOSSIBLE"<<endl;
            
        }
		Output.close();
	}
	else
	{
		cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
	}
    return 0;
}
