#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <iterator>
#include <fstream>
#include <cmath>
using namespace std;





int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++) {
        cout<<"Case #"<<cas<<": ";
        int N,Q;
        cin>>N>>Q;
        vector<long long> E(N),S(N);
        vector<vector<long long > > mat(N,vector<long long >(N));
        for(int c=0;c<N;c++) cin>>E[c]>>S[c];
        for(int c=0;c<N;c++) for(int c2=0;c2<N;c2++) cin>>mat[c][c2];

        int trash;
        cin>>trash>>trash;
        vector<double> dp(N,1e18);
        dp[0]=0;
        for(int c=0;c<N;c++) {
            long long  d = 0;
            int i = c;
            while(i+1<N) {
                d+= mat[i][i+1];
                if(d > E[c]) break;
                dp[i+1] = min(dp[i+1],static_cast<double>(d)/static_cast<double>(S[c])+dp[c]);
                i++;
            }
        }
        cout<<fixed<<setprecision(10)<<dp[N-1]<<endl;
    }

}
