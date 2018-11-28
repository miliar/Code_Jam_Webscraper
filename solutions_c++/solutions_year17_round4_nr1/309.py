#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double rl;

int true_mod(int a, int b)
{
    a%=b;
    if(a<0) a+=b;
    return a;
}

const int MX=109;
typedef tuple<int, int, vector<int>> tp;
map<tp, int> M;

int solve(int left, int P, vector<int> a)
{
    tp foo=tp(left, P, a);


    int res;
    if(M.find(foo)!=M.end()) res=M[foo];
    else
    {
        bool all_zero=true;
        for(int i=0; i<3; i++) if(a[i]!=0) all_zero=false;
        if(all_zero)
        {
            res=0;
        }
        else
        {
            res=0;
            if(left==0) res=1;

            int best=0;
            for(int i=0; i<3; i++)
            {
                vector<int> a_new=a;
                if(a_new[i]<=0) continue;
                a_new[i]--;

                int left_new=true_mod(left-(1+i), P);

                best=max(best, solve(left_new, P, a_new));
            }

            res=res+best;
        }

        M[foo]=res;
    }

    return res;
}

int N, P;
int G[MX];

//int dp[4][MX][MX][MX][MX];

int solve()
{

    //for(int i=0; i<4; i++) A[i]=0;
    //A=B=C=D=0;
    vector<int> A(3);

    int res=0;

    for(int i=0; i<N; i++)
    {
        int md=G[i]%P;
        if(md==0) res++;
        else A[md-1]++;
    }

    return res+solve(0, P, A);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        //int N;
        //cin >> N;
        //int result=solve(N);
        cin >> N >> P;
        for(int i=0; i<N; i++) cin >> G[i];
        int result=solve();
        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}
