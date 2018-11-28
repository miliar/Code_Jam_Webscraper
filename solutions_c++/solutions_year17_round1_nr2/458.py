#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

int start(int q, int r){
    return (10*q + 11*r-1)/(11*r);
}

int end(int q, int r){
    return (10*q)/(9*r);
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, P;
        cin >> N >> P;
        vector<int> R(N);

        for(int i=0;i<N;i++) cin >> R[i];

        vector<int> Qrow(P,0);
        vector<vector<int> > Q(N, Qrow);

        for(int i=0;i<N;i++){
            for(int j=0;j<P;j++){
                cin >> Q[i][j];
            }
        }

        for(int i=0;i<N;i++){
            sort(Q[i].begin(), Q[i].end());
        }
        
        int ans = 0;
        vector<int> inds(N, 0);

        bool done = false;
        while(!done){
            int sind = 0;
            int eind = 0;
            int smax = start(Q[0][inds[0]], R[0]);
            int emin = end(Q[0][inds[0]], R[0]);

            for(int i=0;i<N;i++){
                int st = start(Q[i][inds[i]], R[i]);
                int e = end(Q[i][inds[i]], R[i]);
                if(st>smax){
                    smax = st;
                    sind = i;
                }
                if(e<emin){
                    emin = e;
                    eind = i;
                }
            }

            if(smax>emin || emin==0){
                // throw away eind
                inds[eind]++;
            }else{
                // make kit
                ans ++;
                for(int i=0;i<N;i++) inds[i]++;
            }

            for(int i=0;i<N;i++){
                if(inds[i]==P){
                    done = true;
                }
            }
        }

        
        cout << "Case #" << t << ": " << ans << endl;
        
    }

    return 0;
}