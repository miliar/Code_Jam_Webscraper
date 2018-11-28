#include<bits/stdc++.h>
using namespace std;
double T[1005][1005];
double N[1005][2];
double pi = 3.1415926535;
double pole (double r, double h)
{
    return 2*pi*r*h;
}
vector < pair <double, int> > V;
int main(void)
{
    int t; scanf("%d", &t);
    for(int z = 1; z <= t; z++){
        
    V.clear();
    int n, k; 
    scanf("%d%d", &n, &k);
    for(int i = 0; i < n; i++)
    {
            double a,b;
            scanf("%lf%lf", &a, &b);
            N[i][0] = a;
            N[i][1] = b;
            V.push_back(make_pair( -pole(a,b), i));
    }
     sort(V.begin(), V.end());
    
     double ans = 0;
     
     for(int i = 0; i < n; i++)
     {
         double temp = N[i][0]*N[i][0]*pi + pole(N[i][0], N[i][1]);
         int ile = 1;
         for(int j = 0; j < V.size() && ile < k; j++)
         {
             int num = V[j].second;
             if(N[num][0] <= N[i][0] && num != i)
             {
                ile++;
                temp -= V[j].first;
            
             }
         }
         if(ile == k)
             ans = max(ans, temp);
     }  
     
//     for(int i = 0; i < n; i++)
//         T[0][i] = pole(N[i][0], N[i][1]) + pi*N[i][0]*N[i][0];
//     
//     for(int i = 1; i < k; i++)
//     {
//         for(int j = 0; j < n; j++)
//         {
//             for(int k = 0; k < n; k++)
//             {
//                 T[i][j] = max(T[i][j], T[i-1][k] + pole(N[j][0], N[j][1]));
//             }
//         }
//     }
//     
//     for(int i = 0; i < n; i++)
//         ans = max (ans, T[k-1][i]);
    
    printf("Case #%d: %lf\n",z, ans);}
    

return 0;
}