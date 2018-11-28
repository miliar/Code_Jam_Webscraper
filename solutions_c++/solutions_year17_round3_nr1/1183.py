#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    int casos;
    cin >> casos;
    
    double bases[2000];
    double lados[2000];
    bool tomado[2000];
        
    for(int caso=1;caso<=casos;caso++)
    {
        int n,k;
        cin >> n >> k;
        
        
        double areaTotal=0;
        double baseTotal=0;
        
        
        for(int i=0;i<n;i++)
        {
            double r,h;
            cin  >> r >> h;
            bases[i] = r*r*3.14159265358979323846;
            lados[i] = h*3.14159265358979323846*2*r;
            tomado[i]=false;
        }
        
        
        for(int i=0;i<k;i++)
        {
            double maximoAd = 0;
            int tomar = -1;
            for(int k=0;k<n;k++)
            {
                   if(!tomado[k])
                   {
                       if(max(0.0,bases[k]-baseTotal)+lados[k] > maximoAd)
                       {
                         maximoAd=  max(0.0,bases[k]-baseTotal)+lados[k];
                         tomar = k;
                       }
                   }
            }
            tomado[tomar]=true;
            baseTotal= max(bases[tomar],baseTotal);
            areaTotal+=maximoAd;
         
        }
        printf("Case #%d: %.9lf\n",caso,areaTotal);
    }
    return 0;
}
