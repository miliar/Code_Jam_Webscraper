#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N,K;
        cin>>N>>K;

        priority_queue<int> pque;
        pque.push(N);

        for(int j=0;j<K-1;++j){
            int num = pque.top();
            pque.pop();
            if(num==2){
                pque.push(1);
            }else if(num==1){

            }else{
                --num;
                pque.push(num/2);
                pque.push(num-num/2);
            };
        }

        int n=pque.top();
        int a1,a2;
        if(n==1){
            a1=0;
            a2=0;
        }else if(n==2){
            a1=1;
            a2=0;
        }else{
            --n;
            a1=std::max(n/2,n-n/2);
            a2=std::min(n/2,n-n/2);
        }

        cout << "Case #" << i + 1 << ": "<<a1<<' '<<a2<<'\n';
    }
    return 0;
}