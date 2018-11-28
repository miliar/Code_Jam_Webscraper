#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
    long long ins, cur, biu;

    cin >> ins;

    for (int i=0;i<ins;i++) {
        cin >> cur;

        if (cur<0) while (true) {}

        for (int b=0; b<20; b++) {
            if (cur==0) cur=biu;

            bool cont=true;
            long long pla=1, sha=cur;
            int gim=0;
            biu=0;

            while (sha>0) {
                gim++;
                sha/=10;        
            }

            gim-=1;

            pla = pow(10,gim); 

            while (gim>0) {
                long long powl = pow(10,gim);
                long long powm = pow(10,gim-1);

                //cout << cur/powl << " " << (cur/powm)%10 << "\n";

                if ((cur/powl)>((cur/powm)%10)) {
                    //cout << cur-(cur%powl)-1 << "\n";

                    cur=cur-(cur%powl)-1;
                }        

                biu = biu+((cur/powl)*pla);

                pla = pla/10;
                cur = cur%powl;
                gim--;
            }

            biu += cur;

            cur=0;
        }

        cout << "Case #" << i+1 << ": " << biu << "\n"; 
    }
}
