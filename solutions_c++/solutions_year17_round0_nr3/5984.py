#include <iostream>
#include <queue>

using namespace::std;

int main() {
    int T;
    cin>>T;
    long long int N, K;
    for (int i = 1; i <= T; i++) {
        cin>>N>>K;
        long long int curr_max = N / 2;
        long long int curr_min = N / 2;
        if (curr_max + curr_min == N) {
            curr_min -= 1;
        }
        priority_queue<int> queue;
        queue.push(curr_max);
        queue.push(curr_min);

        for (int j = 1; j < K; j++) {
            int current = queue.top();
            queue.pop();
            curr_max = current / 2;
            curr_min = current / 2;
            if (curr_max + curr_min == current) {
                curr_min -= 1;
            }
            queue.push(curr_max);
            queue.push(curr_min);
        }
        cout<<"Case #"<<i<<": "<<curr_max<<" "<<curr_min<<'\n';
    }
}
