#include<bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 1000000000;


struct MaxFlow {
  int N;
  VVI cap, flow;
  VI dad, Q;

  MaxFlow(int N) :
    N(N), cap(N, VI(N)), flow(N, VI(N)), dad(N), Q(N) {}

  void AddEdge(int from, int to, int cap) {
   // cout << "! " << from << " " << to << endl;
    this->cap[from][to] += cap;
  }

  int BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), -1);
    dad[s] = -2;

    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < N; i++) {
        if (dad[i] == -1 && cap[x][i] - flow[x][i] > 0) {
          dad[i] = x;
          Q[tail++] = i;
        }
      }
    }

    if (dad[t] == -1) return 0;

    int totflow = 0;
    for (int i = 0; i < N; i++) {
      if (dad[i] == -1) continue;
      int amt = cap[i][t] - flow[i][t];
      for (int j = i; amt && j != s; j = dad[j])
        amt = min(amt, cap[dad[j]][j] - flow[dad[j]][j]);
      if (amt == 0) continue;
      flow[i][t] += amt;
      flow[t][i] -= amt;
      for (int j = i; j != s; j = dad[j]) {
        flow[dad[j]][j] += amt;
        flow[j][dad[j]] -= amt;
      }
      totflow += amt;
    }

    return totflow;
  }

  int GetMaxFlow(int source, int sink) {
    int totflow = 0;
    while (int flow = BlockingFlow(source, sink))
      totflow += flow;
    return totflow;
  }
};

int main(){
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){

       int N, P;
       cin >> N >> P;
       vector<int> R(N);
       
       for(int i=0;i<N;i++)
            cin >> R[i];

       
        vector<vector<int>> packs(N, vector<int>(P));

        for(int i=0;i<N;i++)
            for(int j=0;j<P;j++)
                cin >> packs[i][j];

        // for(int i=0;i<N;i++)
        //     sort(packs[i].begin(), packs[i].end());

        MaxFlow mf(N * P + 2);
        // N*P -> top
        
        for(int i=0;i<P;i++){
            int a,b;
            a = (int) ceil(packs[0][i] / (1.1 * R[0]));
            b = (int) floor (packs[0][i] / (0.9 * R[0]));
            if(b >= a)
                mf.AddEdge(N*P, i, 1);
        }

        // N*P + 1 -> bottom
        for(int i=0;i<P;i++){
            int a,b;
            a = (int) ceil(packs[N-1][i] / (1.1 * R[N-1]));
            b = (int) floor (packs[N-1][i] / (0.9 * R[N-1]));
            if(b >= a)
                mf.AddEdge((N-1)*P + i, N*P+1, 1);
        }

        for(int i=0;i<N-1;i++)
            for(int j=0;j<P;j++){

                int a,b;
                a = (int) ceil(packs[i][j] / (1.1 * R[i]));
                b = (int) floor (packs[i][j] / (0.9 * R[i]));


               // cout << " !!! " << packs[i][j] << " " << R[i] << " -> " << a << " " << b << endl;
                if(a > b)
                    continue;

                for(int j2=0;j2<P;j2++){
                    int a2 = (int) ceil(packs[i+1][j2] / (1.1 * R[i+1]));
                    int b2 = (int) floor(packs[i+1][j2] / (0.9 * R[i+1]));

                    //cout << " !!! " << packs[i][j2] << " " << R[i+1] << " -> " << a2 << " " << b2 << endl;

                    if(a2 > b2)
                       continue;

                    if( (a2 >= a && a2 <= b) || (b2 >=a && b2<=b) || (a >= a2 && a<=b2) || (b >=a2 && b<=b2) )
                        mf.AddEdge(i*P + j, (i+1)*P + j2 , 1);

                }
            }
            
        int answer = (int) mf.GetMaxFlow(N*P , N*P+1);
        cout << "Case #" << t+1 << ": " << answer << endl; 
    }
    
    
    return 0;
}  