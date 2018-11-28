#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    freopen("C-small-1-attempt0.in.txt","r",stdin);
    freopen("outsmall.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N,K;
        cin >> N >> K;
        double U;
        cin >> U;
        double arr[N];
        for(int i = 0; i < N; i++){
            cin >> arr[i];
        }
        sort(arr,arr+N);
        double maxi = 1;
        for(int i = 0; i < N; i++){
            maxi *= arr[i];
        }
        for(int i = 0; i < N; i++){
            double sum = 0;
            for(int j = 0; j <= i; j++){
                sum += arr[j];
            }
            sum = min(sum+U,(double)(i+1));
            if(sum/(double)(i+1) < arr[i]) continue;
            double temp = 1;
            for(int j = 0; j <= i; j++){
                temp *= (sum/(double)(i+1));
            }
            for(int j = i+1; j < N; j++){
                temp *= arr[j];
            }
            maxi = max(maxi,temp);
        }
        cout << std::fixed;
        cout << std::setprecision(6);
        cout << "Case #" << t << ": " << maxi << "\n";
    }
    return 0;
}
