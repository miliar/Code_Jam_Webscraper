#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
const string im = "IMPOSSIBLE";
int main()
{
    int T, K;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        DI(t)
//----  wczytaj();
        string pk;
        cin >> pk >> K;
        vector<bool> pkb(pk.size());
        for(int i =0 ; i < pk.size(); ++i)
            if(pk[i] == '+')
                pkb[i] = true;
        int ret = 0;
        for(int i =0 ; i< pkb.size() - K + 1; ++i)
        {
            if(!pkb[i])
            {
                for(int k =0 ; k< K; ++k)
                    pkb[i+k]= (!pkb[i+k]);
                ++ret;
            }
        }
        printf("Case #%d: ",t);
        for(int k =1 ; k<= K; ++k)
            if(!pkb[pkb.size()-k])
                goto impossible;

        cout << ret << endl;
        continue;
    impossible:
        cout << im << endl;
    }
    return 0;
}
