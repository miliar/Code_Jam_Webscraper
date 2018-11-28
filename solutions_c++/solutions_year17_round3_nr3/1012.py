#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,k;
    int casos;
    cin >> casos;
    double sss = 0;
    for(int caso=1;caso<=casos;caso++)
    {
   
        cin >> n >> k;
        double u ;
        cin >> u;
    
        
        vector<double> v ;
        for(int i=0;i<n;i++)
        {
            double r ;
            cin >> r;
            v.push_back(r);
        }
        
        sort(v.begin(),v.end());
        v.push_back(v[v.size()-1]);
        for(int i=0;i<n;i++)
        {
          
          
            double sumar = v[i+1]-v[i];
            
            if(u<sumar*(i+1))
            {
              
                for(int k=0;k<=i;k++)
                {
                    v[k]+=u/(i+1);
                }
                  u=0;
            }
            else
            {
                u-=sumar*(i+1);
                for(int k=0;k<=i;k++)
                {
                    v[k]+=sumar;
                }
            }
            
         
                
        }
        if(u!=0)
        {
            u/=(double)n;
        }
        double p = 1;
        for(int i=0;i<n;i++)
        {
            p*=(v[i]+u);
             //cout << v[i]+u  << " || " << p<< endl;
        }
       sss+=p;
        printf("Case #%d: %lf\n",caso,p);
        
    }

  return 0;
}