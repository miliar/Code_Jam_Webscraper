#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;



int n,p;
int r[51];

int a[51][51];
int q[51];


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        printf("Case #%d: ",test);
        cin >> n >> p;
        for(int i=0;i<n;++i)
            cin >> r[i];
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<p;++j)
                cin >> a[i][j];
            sort(a[i], a[i]+p);
        }

        memset(q,0,sizeof(q));

        int ans=0;
        int k = 1;
        bool ok = true;
        while(ok)
        {
            bool nice=true;
            for(int i=0;i<n;++i)
            {
                if(10*a[i][q[i]] < r[i]*k*9 || 10*a[i][q[i]] > r[i]*k*11)
                    nice=false;
            }
            if(nice)
            {
                ans++;
                for(int i=0;i<n;++i)
                {
                    q[i]++;
                    if(q[i]==p)
                        ok=false;
                }
                if(!ok)
                    break;
            }

            for(int i=0;i<n;++i)
            {
                while(10*a[i][q[i]] > r[i] * k * 11)
                    k++;
            }

            for(int i=0;i<n;++i)
            {
                while(q[i]<p && 10*a[i][q[i]] < r[i] * k*9)
                    q[i]++;
                if(q[i]==p)
                {
                    ok=false;
                    break;
                }
            }
        }

        printf("%d\n", ans);

    }

}

