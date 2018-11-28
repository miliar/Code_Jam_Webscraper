#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int t;
    cin >> t;
    int g=1;
    while(t--)
    {
        cout << "Case #" << g << ": ";
        g++;
        int n,q;
        cin >> n >> q;
        int e[n];
        int s[n];
        long long int dist[n][n];
        //int dist1[n];
        for (int i=0;i<n;i++)
        {
            cin >> e[i] >> s[i];
        }
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<n;j++)
            {
                cin >> dist[i][j];
                if (dist[i][j]==-1) dist[i][j]=1e18;
            }
        }
        for (int k=0;k<n;k++)
        for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);

        double gr[n][n];
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<n;j++)
            {
                if (i==j){gr[i][j]=0;continue;}
                if (dist[i][j]<=e[i])
                {
                    gr[i][j]=(double)dist[i][j]/(double)s[i];
                }
                else gr[i][j]=1e18;
            }
        }
        for (int k=0;k<n;k++)
        for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
        gr[i][j]=min(gr[i][j],gr[i][k]+gr[k][j]);
        while(q--)
        {
            int u,v;
            cin >> u >> v;
            u--;
            v--;
            printf("%.8f ",gr[u][v]);
        }
        cout << endl;
    }
    return 0;
}
