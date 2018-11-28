#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    int T; cin >> T;
    for(int ts=1; ts<=T; ts++) {
        int N,P; cin >> N >> P;
        vector<int> R(N);
        vector<vector<int> > Q(N, vector<int>(P));
        for(int i=0; i<N; i++) cin >> R[i];
        for(int i=0; i<N; i++) for(int j=0; j<P; j++) cin >> Q[i][j];
        //for(int i=0; i<N; i++) for(int j=0; j<P; j++) Q[i][j] = Q[i][j]*100.0/R[i];
        for(int i=0; i<N; i++) sort(Q[i].begin(), Q[i].end());
        vector<int> Qi(N);
        int ret=0;
        for(int size=1; size<=1000000; size++) {
            for(int i=0; i<N; i++) while((Qi[i]<P) && (Q[i][Qi[i]]*100 < 90*size*R[i])) Qi[i]++;
            bool valid=true;
            bool done=false;
            for(int i=0; i<N; i++) if(Qi[i]>=P) done=true;
            if(done) break;
            for(int i=0; i<N; i++) if(Q[i][Qi[i]]*100 > 110*size*R[i]) valid=false;
            if(valid) {
                ret++;
                for(int i=0; i<N; i++) Qi[i]++;
                size--;
            }
        }
        cout << "Case #" << ts << ": " << ret << endl;
    }
}
