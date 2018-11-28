#include <cstdio>
#include <iostream>

#include <queue>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        long long int N, K;
        cin >> N >> K;
        if(K > N / 2) printf("Case #%d: 0 0\n", i+1);
        else {
            priority_queue<long long int> p;
            p.push(N);
            int count = 1;
            while(count < K) {
                long long int num = p.top();
                p.pop();
                long long int left = (num-1)/2;
                long long int right = num-1-left;
                p.push(right);
                p.push(left);
                count++;
            }

            long long int left = (p.top()-1)/2;
            long long int right = p.top()-1-left;
            printf("Case #%d: %lld %lld\n", i+1, right, left);
        }
    }
}
