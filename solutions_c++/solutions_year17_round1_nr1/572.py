#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main()
{
    ifstream fin("test.in");
    ofstream fout("rez.out");
    int t;
    fin>>t;
    int T=t;
    while(t--){
        int n,m;
        fin>>n>>m;
        string mapa[n];
        for(int ctr1=0;ctr1<n;ctr1++)
            fin>>mapa[ctr1];
        for(int ctr1=0;ctr1<n;ctr1++){
            char last = -1;
            for(int ctr2=0;ctr2<m;ctr2++){
                if (mapa[ctr1][ctr2] != '?')
                    last=mapa[ctr1][ctr2];
                else if (last != -1)
                    mapa[ctr1][ctr2]=last;
            }
            last = -1;
            for(int ctr2=m-1;ctr2>=0;ctr2--){
                if (mapa[ctr1][ctr2] != '?')
                    last=mapa[ctr1][ctr2];
                else if (last != -1)
                    mapa[ctr1][ctr2]=last;
            }
        }
        for(int ctr2=0;ctr2<m;ctr2++){
            char last = -1;
            for(int ctr1=0;ctr1<n;ctr1++){
                if (mapa[ctr1][ctr2] != '?')
                    last=mapa[ctr1][ctr2];
                else if (last != -1)
                    mapa[ctr1][ctr2]=last;
            }
            last = -1;
            for(int ctr1=n-1;ctr1>=0;ctr1--){
                if (mapa[ctr1][ctr2] != '?')
                    last=mapa[ctr1][ctr2];
                else if (last != -1)
                    mapa[ctr1][ctr2]=last;
            }
        }

        fout<<"Case #"<<T-t<<":\n";
        for(int ctr1=0;ctr1<n;ctr1++)
            fout<<mapa[ctr1]<<"\n";
        cout<<"Case #"<<T-t<<": Done\n";
    }
    fin.close();
    fout.close();
    return 0;
}
