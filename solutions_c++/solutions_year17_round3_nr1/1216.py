#include <bits/stdc++.h>

using namespace std;

#define PI acos(-1)

typedef pair<int, int> pi;


pi input[1000];  // radius, height
int N,K;

int main(){
    int cases;
    scanf("%d", &cases);

    for(int e = 0; e<cases; e++){
        scanf("%d %d", &N, &K);
        for(int i = 0; i<N; i++){
            scanf("%d %d", &input[i].first, &input[i].second);
        }
        sort(input, input+N);
        // printf("Done sorting\n");
        double best = 0;

        for(int i = N-1; i>=0; i--){
            double ans = 0;
            ans += PI * input[i].first * input[i].first;
            ans += 2 * PI * input[i].first * input[i].second;
            priority_queue<double> pq;
            for(int j = i-1; j>=0; j--){
                double this_add = 2 * PI * input[j].first * input[j].second;
                pq.push(this_add);
            }

            for(int k = 0; k<K-1 && !pq.empty(); k++){
                double this_add = pq.top();
                pq.pop();
                ans += this_add;
            }

            best = max(best, ans);
        }

        printf("Case #%d: %f\n",e+1, best);
    }



    return 0;
}