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

long long int res0,res1;

void intervalle(long long A, long long B, long long K){
    if(K == 1) {
        long long int mid = (A+B+1LL)/2LL;
        long long int ecart1 = abs(mid-A);
        long long int ecart2 = abs(mid-B);
        res0=max(ecart1,ecart2);
        res1=min(ecart1,ecart2);
        return;
    }
    if((K&1) == 0) {
        intervalle(A,(A+B+1LL)/2LL-1,K/2);
    } else {
        intervalle((A+B+1)/2+1,B,K/2);
    }
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++) {
        cout<<"Case #"<<cas<<": ";
        long long a,b;
        cin>>a>>b;
        intervalle(0,a-1,b);
        cout<<res0<<" "<<res1<<endl;
    }

}
