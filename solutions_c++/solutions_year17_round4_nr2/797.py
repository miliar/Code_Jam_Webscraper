#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

vector<int> adjList[1010];

int main()
{
    ifstream fin("test.in");
    ofstream fout("rez.out");
    int t;
    fin>>t;
    int T=t;
    int n,m,c;
    while(t--){
        fin>>n>>c>>m;
        int ar[n];
        for(int ctr1 = 0; ctr1 < c; ctr1++)
            adjList[ctr1].clear();
        memset(ar,0,sizeof(ar));
        int p,b;
        for (int ctr1 = 0; ctr1 < m; ctr1++) {
            fin>>p>>b;
            p--,b--;
            adjList[b].push_back(p);
            ar[p]++;
        }
        int rides = 0;
        int acc_sum = 0;
        for(int ctr1 = 0; ctr1 < n; ctr1++) {
            acc_sum += ar[ctr1];
            rides = max(rides, acc_sum/(ctr1+1));
        }
        for(int ctr1 = 0; ctr1 < c; ctr1++) {
            rides = max(rides,(int) adjList[ctr1].size());
        }
        int left[n];
        for(int ctr1 = 0; ctr1 < n; ctr1++)
            left[ctr1] = rides;
        int rez = 0;
        for(int ctr1 = 0; ctr1 < c; ctr1++) {
            for(auto it:adjList[ctr1]) {
                if(left[it])
                    left[it]--;
                else {
                    while(left[it] == 0)
                        it--;
                    left[it]--;
                    rez++;
                }
            }
        }
        fout<<"Case #"<<T-t<<": "<<rides<<" "<<rez<<"\n";
        cout<<"Case #"<<T-t<<": "<<rides<<" "<<rez<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
