#include <iostream>
#include <vector>
#include <queue>


typedef long long ll;
using namespace std;


int main() {
//    small input
//    freopen("test1.txt","r",stdin);
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("Csmall2.out","w",stdout);
    int tt;

    cin >> tt;
    int order = 1;
    while(tt-- > 0){
        ll num;
        ll N,K;
        priority_queue <ll> Q;
        cin >> N;
        cin >> K;
        Q.push(N);
        while(--K >= 0){
            ll val = Q.top();
            Q.pop();
            Q.push(val/2);
            Q.push((val - 1)/2);
            if(K == 0){
                cout<<"Case #"<<(order++)<<": "<<(val)/2 << " "<< (val - 1)/2 <<endl;
                break;
            }
        }
    }
}