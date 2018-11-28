#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, C, M;
        cin >> N >> C >> M;

        vector<int> ticketPs(N, 0);
        vector<int> ticketBs(C, 0);

        for(int i=0;i<M;i++){
            int P, B;
            cin >> P >> B;
            ticketPs[P-1]++;
            ticketBs[B-1]++;
        }

        int trains = 0;
        for(int i=0;i<C;i++){
            if(ticketBs[i] > trains)
                trains = ticketBs[i];
        }

        int cum=0;
        for(int i=0;i<N;i++){
            cum+=ticketPs[0];
            int needed = (cum+i)/(i+1);
            if(needed > trains)
                trains = needed;
        }

        int promos = 0;
        for(int i=0;i<N;i++){
            if(ticketPs[i] > trains){
                promos += ticketPs[i] - trains;
            }
        }
        
        cout << "Case #" << t << ": " << trains << " " << promos << endl;

    }

    return 0;
}