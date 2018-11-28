#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
int heap[10000000], hpn;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    
    int n, k;
    for(int f = 1; f <= T; f++){
        cin >> n >> k;
        cout << "Case #" << f << ": ";
        if(n == k){
            cout << "0 0" << endl;
            continue;
        }
        
        hpn = 0;
        heap[hpn++] = n;
        for(int i = 0; i < k - 1; i++){
            int len = heap[0] - 1;
            pop_heap(heap, heap+hpn);
            hpn--;
            int L = len / 2;
            int R = len - L;
            if(L > 0){
                heap[hpn++] = L;
                push_heap(heap, heap+hpn);
            }
            if(R > 0){
                heap[hpn++] = R;
                push_heap(heap, heap+hpn);
            }
        }
        
        int len = heap[0] - 1;
        pop_heap(heap, heap+hpn);
        int L = len / 2;
        int R = len - L;
        cout << R << " " << L << endl;
    }

    return 0;
}
