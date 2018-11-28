#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
#include <vector>
using namespace std;



int main()
{
    //read
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++){
        int te;
        int Ac,Aj, Cfrom[3], Cto[3], Jfrom[3], Jto[3];
        cin >> Ac >> Aj;
        for (int i=1;i<=Ac;i++) cin >> Cfrom[i] >> Cto[i];
        for (int i=1;i<=Aj;i++) cin >> Jfrom[i] >> Jto[i];

        

        if (Ac+Aj==1) te = 2;
        else {
            if (Ac==1 && Aj==1) te = 2;
            else {

                if (Ac==2){ 
                    if (Cfrom[1] > Cfrom[2]){ 
                        swap(Cfrom[1],Cfrom[2]);
                        swap(Cto[1],Cto[2]);
                    }
                    if (Cto[2]-Cfrom[1]<=720 || Cto[1]+1440-Cfrom[2]<=720) 
                        te = 2;
                    else 
                        te = 4;
                }
                else {
                    if (Jfrom[1] > Jfrom[2]){
                        swap(Jfrom[1],Jfrom[2]);                   
                        swap(Jto[1],Jto[2]);                   
                    }
                    if (Jto[2]-Jfrom[1]<=720 || Jto[1]+1440-Jfrom[2]<=720) 
                        te = 2;
                    else 
                        te = 4;
                }


            }


        }

        

        cout << "Case #" << t << ": " << te << endl;

    }


    return 0;
}
