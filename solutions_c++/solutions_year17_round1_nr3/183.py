#include<iostream>
#include<cstdio>

using namespace std;

int a[100];


int dc(int x, int y)
{
    int ret = x-y;
    if (ret <0 ) ret = 0;
    return ret;
}
int main()
{
  freopen("c.in.txt","r",stdin);
  freopen("c.out","w",stdout);
  int t;
  scanf("%d", &t);
    int hd,ad,hk,ak,b,d;

 
  for (int tt = 0; tt < t; tt++)
    {
    
      scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);
        int ans = 1000;
        int ud;
        int ub;
        if (d != 0) ud = ak / d + 1; else ud = 0;
        if (b != 0) ub = hk / b + 1; else ub = 0;
        for (int dd = 0; dd <= ud; dd++)
            for (int bb = 0 ; bb <= ub; bb++)
            {
                int r = 0;
                int sd = 0;
                int sb = 0;
                int gd = hd;
                int cd = ad;
                int gk = hk;
                int ck = ak;
                while (r <= ans && sd < dd)
                {
                   
                    r++;
                    if (gd - dc(ck,d) <= 0) gd  = hd;
                    else {
                        ck = dc(ck,d);
                        sd++;
                    }
                    gd -= ck;
                    if (gd <=0)
                    {
                        break;
                    }
                }
                if (sd == dd)
                {
                    while (r <=ans && sb < bb)
                    {
                        
                        r++;
                        if (gd - ck <= 0) gd = hd;
                        else{
                            cd+= b;
                            sb++;
                        }
                        gd-=ck;
                        if (gd <= 0)
                            break;
                    }
                    if (sb == bb)
                    {
                        while (r <= ans && gk > 0)
                        {
                            r++;
                            if (gd - ck <= 0 && gk - cd >0) gd = hd; else {gk-= cd;}
                            
                            gd -=ck;
                            if (gd <=0 && gk > 0) break;
                        }
                        if (gk <= 0 && r < ans) ans = r;
                    }
                }
            }
      cout << "Case #" << tt+1 << ": ";
        if (ans == 1000) cout << "IMPOSSIBLE\n"; else cout << ans << endl;
    }
}
