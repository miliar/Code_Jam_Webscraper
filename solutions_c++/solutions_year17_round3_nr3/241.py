#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int ncase;
    scanf("%d", &ncase);
    
    for(int cases=1; cases<=ncase; cases++)
    {
        int n, m;
        double u, ans=1;
        scanf("%d%d%lf", &n, &m, &u);
        vector<double> p(n);
        
        for(int i=0; i<n; i++)
            scanf("%lf", &p[i]);
        
        sort(p.begin(), p.end());
        p.push_back(1);
        /*
        for(int i=n-1; i>=0; i--)
        {
            if( u<=(1-p[i])*(i+1) )
            {
                for(int j=0; j<=i; j++)
                    p[j]+=u/(i+1);
                
                break;
            }
            else
            {
                u-=(1-p[i])*(i+1);
                
                for(int j=0; j<=i; j++)
                    p[j]+=1-p[i];
            }
        }
        */
        for(int i=0; i<n; i++)
        {
            if( u<=(p[i+1]-p[i])*(i+1) )
            {
                for(int j=0; j<=i; j++)
                    p[j]+=u/(i+1);
                
                break;
            }
            else
            {
                u-=(p[i+1]-p[i])*(i+1);
                
                for(int j=0; j<=i; j++)
                    p[j]=p[i+1];
            }
        }
        
        for(int i=0; i<n; i++)
            ans*=p[i];
        
        printf("Case #%d: %.10f\n", cases, ans);
    }
}

/*

2

4 4
1.4000
0.5000 0.7000 0.8000 0.6000

2 2
1.0000
0.0000 0.0000

2 1
0.0000
0.9000 0.8000

2 1
0.1000
0.4000 0.5000

*/
