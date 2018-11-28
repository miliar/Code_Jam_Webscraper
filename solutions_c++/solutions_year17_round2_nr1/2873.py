#include<bits/stdc++.h>
using namespace std;
vector <pair <int, int> > V;
double ans[1005];
int main()
{
    int t;
    scanf("%d", &t);
    for(int a = 1; a <= t; a++)
    {
        V.clear();
        int d,n; 
        scanf("%d%d", &d, &n);
        for(int k = 0; k < n; k++)
        {
            int ki, si;
             scanf("%d%d", &ki, &si);
            V.push_back(make_pair(ki, si));
        }
        sort(V.begin(), V.end());
        double total = 0;
        ans[V.size()-1] = (double)(d-V[V.size()-1].first)/ (V[V.size()-1].second);
        for(int k = V.size()-2; k >=0; k--)
        {
            ans[k] = max(ans[k+1], (double)(d-V[k].first)/ V[k].second);
        }

        printf("Case #%d: %lf\n", a, (double)d/ans[0]);
        
    }
    return 0;
}