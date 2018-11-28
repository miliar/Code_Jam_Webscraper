#include <iostream>
#include <queue>
using namespace std;

string dfs(long long int N, long long int K, priority_queue<long long int > &pq){
    pq.push(N);
    long long int half;
    while(K-- > 1){
        N = pq.top();
        pq.pop();
        half = N / 2;
        long long int left_grid = (N & 1) == 0? half - 1 : half;
        long long int right_grid = N - left_grid - 1;
        //if(pq.size() < 64){
            pq.push(left_grid);
            pq.push(right_grid);
        //}
    }
    N = pq.top();
    half = N / 2;
    string left = to_string (half);
    string right = (N & 1) == 0 ? to_string(half - 1) : to_string(half); 
    return left + " " + right;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, count = 1;
    cin >> t;
    while(t--){
        long long int N, K;
        priority_queue<long long int> pq;
        cin >> N >> K;
        string res = dfs(N, K, pq);
        cout << "Case #" << count << ": " << res << endl;
        count ++;
    }

    return 0;
}