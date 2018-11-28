#include <bits/stdc++.h>
using namespace std;

typedef double rl;

int N, Q;
const int MX=109;
int E[MX], S[MX];
int D[MX][MX];
int L[MX];

struct horse
{
    int E;
    int S;
    rl total_time;
};

rl solve()
{
    vector<horse> V;
    {
        horse tmp{.E=E[0], .S=S[0], .total_time=0.0};
        V.push_back(tmp);
    }

    cerr << "-----------" << endl;
    for(int i=0; i+1<N; i++) cerr << L[i] << endl;
cerr << "-----------" << endl;

    for(int i=0; i<N; i++)
    {
        vector<horse> V_new;

        cerr << "ii:" << i << endl;
        for(auto h: V)
        {
            cerr << h.E << ' ' << h.S << ' ' << h.total_time << endl;
        }
        cerr << "---" << endl;;

        for(auto h: V)
        {
            horse hh=h;
            hh.E-=L[i];
            hh.total_time+=(L[i]+0.0)/h.S;

            if(hh.E<0) continue;
            V_new.push_back(hh);
        }

        assert(!V_new.empty());

        rl best_time=1E100;
        for(auto h: V_new)
        {
            best_time=min(best_time, h.total_time);
        }

        if(i==N-2) return best_time;

        horse tmp{.E=E[i+1], .S=S[i+1], .total_time=best_time};
        V_new.push_back(tmp);

        V=V_new;
    }

    return -1.0;
}

int main()
{
    cout << setprecision(10);

    freopen("C-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        cin >> N >> Q;
        for(int i=0; i<N; i++)
        {
            cin >> E[i] >> S[i];
        }

        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++) cin >> D[i][j];
        }

        for(int i=0; i+1<N; i++) L[i]=D[i][i+1];

        for(int i=0; i<Q; i++)
        {
            int U, V;
            cin >> U >> V;
        }

        if(Q!=1) assert(false);//continue;
        rl res=solve();


        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
