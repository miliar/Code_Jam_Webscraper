#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for (int test=1; test<=T; test++)
    {
        int Hd, Ad, Hk, Ak, B, D;
        cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
        int oo = 99999999;
        int ans = oo;
        for (int Bc=0; Bc<=100; Bc++)
        for (int Dc=0; Dc<=100; Dc++)
        {
            int hd = Hd;
            int ad = Ad;
            int hk = Hk;
            int ak = Ak;
            int bc = 0;
            int dc = 0;

            int turn;
            bool win = false;
            for (turn=1; turn<1000; turn++)
            {
                if (!(hk-ad<=0 ||
                      hd-ak>0 ||
                      (dc<Dc && hd-max(0,ak-D)>0)))
                {
                    hd = Hd;
                }
                else if (dc<Dc)
                {
                    ak = max(0, ak-D);
                    dc++;
                }
                else if (bc<Bc)
                {
                    ad += B;
                    bc++;
                }
                else
                {
                    hk -= ad;
                    if (hk<=0)
                    {
                        win = true;
                        break;
                    }
                }

                hd -= ak;
                if (hd<=0)
                    break;
            }
            if (win)
                ans = min(ans, turn);
        }
        if (ans<oo)
            cout<<"Case #"<<test<<": "<<ans<<endl;
        else
            cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
    }
}
