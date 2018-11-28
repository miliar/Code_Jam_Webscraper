#include<bits/stdc++.h>
using namespace std;
vector <double> V;
int main(void)
{
    int t; scanf("%d", &t);
    for(int z = 1; z <= t; z++){
    double ans = 1.0;
    V.clear();
    int n,k; scanf("%d%d", &n,&k);
    double p; scanf("%lf", &p);
    
    for(int i = 0; i < n; i++)
    {
        double a; scanf("%lf", &a);
        V.push_back(a);
    }
    V.push_back(1.0);
    sort(V.begin(), V.end());
    for(int i = 0; i < n; i++)
    {
        double diff = V[i+1] - V[i];
        double pot = diff*(i+1);
        double roz = min(pot, p)/(i+1);
        for(int j = i; j >= 0; j--)
            V[j] += roz;
        p -= (roz*(i+1));
    }
    
    for(int i = 0; i < n; i++)
        ans *= V[i];
    
    printf("Case #%d: %lf\n",z, ans);}
    

return 0;
}