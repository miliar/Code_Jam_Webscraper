#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int K[10000],S[10000];

struct Node
{
    int k,s;
    bool operator<(const Node&obj)const{return k>obj.k;}
}nodes[10000];
double time[10000];
int main()
{
    ios::sync_with_stdio(false);
    int T,N,D;
    cin >> T;
    int cas=0;
    while(T--)
    {
        printf("Case #%d: ",++cas);
//        cout << "Case #" << ++cas << ": ";
        cin >> D >> N;
        for(int i=0;i<N;++i)
        {
            cin >>nodes[i].k>>nodes[i].s;

        }
        sort(nodes,nodes+N);
        time[0]=double(D-nodes[0].k)/nodes[0].s;
        for(int i=1;i<N;++i)
        {
            time[i]=double(D-nodes[i].k)/nodes[i].s;
            if(time[i]<time[i-1]) time[i]=time[i-1];
        }
        printf("%f\n",D/time[N-1]);
//        cout << D/time[N-1] << endl;
    }
    return 0;
}
