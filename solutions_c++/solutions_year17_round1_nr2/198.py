#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for (int test=1; test<=T; test++)
    {
        int N, P;
        cin>>N>>P;
        vector<int> R(N);
        for (int &r: R)
            cin>>r;
        vector<vector<int>> Q(N, vector<int>(P));
        vector<vector<int>> Qmin(N, vector<int>(P));
        vector<vector<int>> Qmax(N, vector<int>(P));

        for (int i=0; i<N; i++)
        for (int j=0; j<P; j++)
        {
            cin>>Q[i][j];
            //  x*90/100*R[i] <= Q[i][j] <= x*110/100*R[i]
            Qmin[i][j] = Q[i][j]*100/(110*R[i]);
            if (Q[i][j]*100%(110*R[i]) != 0)
                Qmin[i][j]++;
            Qmax[i][j] = Q[i][j]*100/(90*R[i]);

            if (Qmin[i][j]>Qmax[i][j])
                Qmin[i][j] = 99999999;
        }

        int ans = 0;
        vector<vector<bool>> used(N, vector<bool>(P));
        while (true)
        {
            int a = 0;
            for (int i=0; i<N; i++)
            {
                int t = 99999999;
                for (int j=0; j<P; j++)
                if (!used[i][j])
                    t = min(t, Qmin[i][j]);
                if (t < 99999999)
                    a = max(a, t);
            }
            if (a==0)
                break;
            bool ok = true;
            for (int i=0; i<N; i++)
            {
                int best = -1;
                for (int j=0; j<P; j++)
                    if (!used[i][j] && Qmin[i][j]<=a && a<=Qmax[i][j] &&
                        (best==-1 || Qmax[i][j]<Qmax[i][best]))
                        best = j;
                if (best == -1)
                    ok = false;
                else
                    used[i][best] = true;
            }
            if (!ok)
                break;
            ans++;
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}
