#include <iostream>
#include <fstream>
#include <queue>
#include <bitset>
#include <string.h>

using namespace std;

struct state{
    int nr, s;
};

bitset<2048> bs;

int solve(int k, int nr, int n){
    int mask = (1<<k)-1;

    deque<state> q;
    q.push_back({nr, 0});
    bs[nr] = 1;

    while(!q.empty()){
        state crt = q.front();
        q.pop_front();

        if(crt.nr == 0)return crt.s;

        for(int i=0;i<=n-k;i++){
            if(!bs[(crt.nr^(mask<<i))]){
                q.push_back({(crt.nr^(mask<<i)), crt.s+1});
                bs[(crt.nr^(mask<<i))] = 1;
            }
        }
    }

    return -1;
}

int main()
{
    /*ifstream in("in.txt");
    ofstream out("out.txt");*/
    int t;
    cin>>t;

    for(int i=1;i<=t;i++){
        for(int j=0;j<2048;j++)bs[j]=0;

        char str[11];
        int k, nr=0;

        cin>>str;
        cin>>k;

        for(int j=0;str[j]!='\0';j++){
            if(str[j]=='-')nr+=(1<<j);
        }

        int sol = solve(k, nr, strlen(str));
        if(sol!=-1)cout<<"Case #"<<i<<": "<<sol<<"\n";
        else cout<<"Case #"<<i<<": IMPOSSIBLE\n";
    }
    return 0;
}
