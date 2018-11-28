#include <bits/stdc++.h>
using namespace std;

const double pi = 3.1415926;

vector<pair<int, int>> A;
void work(){
    double best = 0;
    int n, k;
    cin >> n >> k;
    A.clear();
    for(int i = 0; i < n; i++){
        int r, h;
        cin >> r >> h;
        A.push_back(make_pair(r, h));
    }

    for(int i = 0; i < n; i++){
        vector<long long int> B;
        for(int j = 0; j < n; j++)
            if(i != j && A[j].first <= A[i].first)
                B.push_back(((long long int)A[j].second) * A[j].first);
        sort(B.begin(), B.end());
        if(B.size() < k-1)
            continue;
        B.push_back(((long long int)A[i].second) * A[i].first);
        double tmp = pi * pow(A[i].first, 2.0);
        for(int j = 0; j < k; j++)
            tmp += 2 * B[B.size()-1-j] * pi;
        best = max(best, tmp);
    }

    printf("%.8lf", best);
}

int main(){

    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        work();
        printf("\n");
    }
    return 0;
}
