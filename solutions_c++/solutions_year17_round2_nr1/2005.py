#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("A-small.in");

int main()
{
    FILE * pFile;
    pFile = fopen ("out.out","w");
    int caso,ncasi;
    in>>ncasi;
    for (caso=1;caso<=ncasi;caso++){
        double minSpeed,tmp;
        double speedAnnie=1100.0/caso;
        int nCavalli, distanza,partenza,velocita;
        in>>distanza>>nCavalli;
        in>>partenza>>velocita;
        minSpeed=(double)distanza/((double)(distanza-partenza)/velocita);
        for (int i=1;i<nCavalli;i++){
            in>>partenza>>velocita;
            tmp=(double)distanza/((double)(distanza-partenza)/velocita);
            if (tmp<minSpeed)
                minSpeed=tmp;
        }

        //printf ("Case # %d: %f\n",caso,minSpeed);
        fprintf (pFile, "Case #%d: %f\n",caso,minSpeed);
    }
    return 0;
}
