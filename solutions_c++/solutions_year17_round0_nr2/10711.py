#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int Cek(int a, int b)
{
    if(a<=b) {
        return 0;
    } else {
        return b+1;
    }
}

long long int kuadrat(int a, int b)
{
    long long int calc=1;

    for(int i=1;i<=b;i++) {
        calc=calc*a;
    }

    return calc;
}

int main()
{
    int T = 0;
    long long int N;
    long long int Na;
    int x = 0;
    bool blasttidy;
    long long int ilasttidy = 1;

    ifstream iFile;
    iFile.open("Small.txt");
    ofstream oFile;
    oFile.open ("Output.txt");

    while (iFile >> N) {
        if(T==0) {
            T=N;
        }
        else {
            x = x+1;
            blasttidy=true;
            Na=N;

            while(blasttidy) {
                int lenN = floor (log10 (abs (N))) + 1;

                if(N==1000) {
                    blasttidy=false;
                    ilasttidy=N-1;
                } else if (lenN == 1) {
                    blasttidy=false;
                    ilasttidy=N;
                } else {
                    int aN[lenN];
                    long long int gMulti;

                    for(int i=1;i<=lenN;i++) {
                        if (i==lenN) {
                            aN[i]=N % 10;
                        } else {
                            gMulti=kuadrat(10,lenN-i);
                            aN[i]=N / gMulti % 10;
                        }
                    }

                    long long int Nallsame=0;
                    for(int i=1;i<=lenN;i++) {
                        if(i==lenN) {
                            Nallsame=Nallsame+aN[1];

                        } else {
                            gMulti=kuadrat(10,lenN-i);
                            Nallsame=Nallsame+(aN[1]*gMulti);
                        }
                    }

                    if(N==Nallsame) {
                        blasttidy=false;
                        ilasttidy=N;
                    } else if (N < Nallsame) {
                        gMulti=kuadrat(10,lenN-1);
                        ilasttidy=((aN[1]-1)*gMulti)+(gMulti-1);
                        blasttidy=false;
                    } else {
                        ilasttidy=0;
                        for(int i=1;i<=lenN;i++) {
                            if(i==lenN) {
                                gMulti=1;
                            } else {
                                gMulti=kuadrat(10,lenN-i);
                            }

                            if(aN[i] <= aN[i+1]) {
                                ilasttidy=ilasttidy + (aN[i]*gMulti);
                            } else{
                                ilasttidy=ilasttidy + (aN[i]*gMulti) - 1;
                                break;
                            }
                        }
                        blasttidy=false;
                    }
                }
            }

            oFile << "Case #" << x << ": " << ilasttidy << endl;
        }
    }

    iFile.close();
    oFile.close();

    return 0;
}
