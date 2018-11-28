#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
ifstream in("C-small.in");


int main()
{
    int caso,ncasi,n,k;
    in>>ncasi;
    FILE * pFile;
    pFile = fopen ("out.out","w");
    vector <double> cores;
    for (caso=1;caso<=ncasi;caso++){
        double result=1,u;
        cores.clear();
        in>>n>>k>>u;
        for (int i=0;i<n;i++){
            double tmp;
            in>>tmp;
            cores.push_back(tmp);
        }
        while(u>0.000001){
            double secondoMin=1,min=1;
            vector<int> posMin;
            for (int i=0;i<n;i++){
                if (cores.at(i)<min){
                    secondoMin=min;
                    min=cores.at(i);
                    posMin.clear();
                    posMin.push_back(i);
                }else if(cores.at(i)==min){
                    posMin.push_back(i);
                }else if (cores.at(i)<secondoMin){
                    secondoMin=cores.at(i);
                }
            }
            if ((secondoMin-min)*posMin.size()>u){
                double toAdd=u/posMin.size();
                for(int i=0;i<posMin.size();i++)
                    cores.at(posMin.at(i))+=toAdd;
                u=0;
            }else{
                u-=(secondoMin-min)*posMin.size();
                for(int i=0;i<posMin.size();i++)
                    cores.at(posMin.at(i))=secondoMin;
            }
        }
        for (int i=0;i<n;i++){result*=cores.at(i); cout<<cores.at(i)<<" ";}
        cout<<endl;
        printf ("Case #%d: %f\n",caso,result);
        fprintf (pFile, "Case #%d: %f\n",caso,result);
    }
    return 0;
}
