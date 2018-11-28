#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    unsigned long long n, k;
    cin >> t;
    for (int z=1; z<=t; ++z){
        cin >> n >> k;

        priority_queue<unsigned long long> max_heap;
        max_heap.push(n);

        while (k>1){
            auto curr = max_heap.top();
            max_heap.pop();

            if (curr & 1){
                max_heap.push(curr/2);
                max_heap.push(curr/2);
            }
            else{
                max_heap.push(curr/2);
                max_heap.push(curr/2-1);
            }
            --k;
        }

        auto curr = max_heap.top();
        auto y = curr/2;
        unsigned long long w;
        if (curr & 1){
            w = y;
        }
        else{
            w = y-1;
        }
        cout << "Case #" << z << ": " << y << " " << w << "\n";
    }
    return 0;
}

