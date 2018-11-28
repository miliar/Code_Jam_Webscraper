#include<bits/stdc++.h>
using namespace std;
int T[1005];
vector < pair <pair <int, int>, int> > V;
vector <pair <int, int> > P;
int main(void)
{
    int t; scanf("%d", &t);
    for(int z = 1; z <= t; z++){
    V.clear();
    P.clear();
    int sumc = 0, sumj = 0;
    
    int c,j; scanf("%d%d", &c,&j);
    for(int i = 0; i < c; i++)
    {
        int a,b; scanf("%d%d", &a, &b);
        V.push_back( make_pair (make_pair(a,b), 0));
        sumj += (b - a);
    }
     for(int i = 0; i < j; i++)
    {
        int a,b; scanf("%d%d", &a, &b);
        V.push_back( make_pair (make_pair(a,b), 1));
        sumc += (b - a);
    }
    sort(V.begin(), V.end());
    pair < pair <int, int>, int > p = V[0];
    p.first.first += 1440;
    p.first.second += 1440;
    V.push_back(p);
    
    int mini = 0;
    for(int i = 0; i < V.size()-1; i++)
    {
        pair < pair <int, int>, int > f = V[i];
        pair < pair <int, int>, int > s = V[i+1];
      //  printf("para %d %d %d %d\n", f.first.first, f.first.second, s.first.first,s.first.second);
        
        if(f.second != s.second) mini++;
        else
        {
            int dist = s.first.first - f.first.second;
          //  printf("dist = %d\n", dist);
            int who = (s.second+1)%2;
            P.push_back(make_pair(-dist, who));
            if(who == 0) sumc += dist;
            else sumj += dist;
            
        }
    }
    
   // printf("cam %d jac %d\n", sumc, sumj);
   // printf("mini = %d\n", mini);
    
    int wyg = max(sumj, sumc);
   // printf("wyg = %d\n", wyg);
    if(wyg >  720)
    {
        
        int zad;
        if(sumj == wyg) zad = 1;
        else zad = 0;
    
        sort(P.begin(), P.end());
        for(int i = 0; i < P.size(); i++)
        {
            if(P[i].second != zad) continue;
            int dist = -P[i].first;
            mini += 2;
            wyg -= dist;
            if(wyg <= 720) break;
        }
    }
    
    
    
    printf("Case #%d: %d\n",z, mini);}
    

return 0;
}