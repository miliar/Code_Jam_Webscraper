#include <iostream>
#include <queue>

using namespace std;

priority_queue<pair<int, int> > P;

pair<int, int> calculaParaK(int N, int K){
    pair<int, int> n;
    int k = 0;
    int dv, md;

    P.push(make_pair(N, 1));

    while(!P.empty()){
        n = P.top();
        P.pop();
        if(n.first == 0)    break;

        while(!P.empty() && (P.top().first == n.first)){
            n.second += P.top().second;
            P.pop();
        }

        k += n.second;
        if(k >= K)  break;

        dv = n.first/2;
        md = n.first%2;

        if(md == 0){
            P.push(make_pair(dv, n.second));
            P.push(make_pair(dv - 1, n.second));
        }else{
            P.push(make_pair(dv, n.second * 2));
        }
    }

    dv = n.first/2;
    md = n.first%2;

    if(md == 0) return make_pair(dv, dv - 1);
    else        return make_pair(dv, dv);
}

int main(){
    int T, N, K;
    pair<int, int> par;

    cin >> T;

    for(int i = 0; i < T; ++i){
        cin >> N >> K;

        par = calculaParaK(N, K);

        cout << "Case #" << i + 1 << ": " << par.first << " " << par.second << endl;

        while(!P.empty()){
            P.pop();
        }
    }
}
