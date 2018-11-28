#include <bits/stdc++.h>

using namespace std;

int main()
{
    
    int casos;
    cin >> casos;
    for(int caso=1;caso<=casos;caso++)
    {
        long long N;
        double D;
        cin >> D >> N;
        double maxSpeed= 19999999999999999;
        
        for(int i=0;i<N;i++)
        {
            double K,C;
            cin >> K >> C;
            double falta= D-K;
            double tiempo = falta/C;
            double maximo = D/tiempo;
            
            maxSpeed= min(maximo,maxSpeed);
        }
        printf("Case #%d: %.06lf\n",caso,maxSpeed);
    }
    return 0;
}