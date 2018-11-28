#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;
vector<int> arr;
vector<vector<int> > gredi;
int main () {
    freopen("/Users/bowbowbow/Downloads/B-small-attempt0.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/B-small-attempt0.out", "w", stdout);
    
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        int N, P;
        cin >> N >> P;
        arr.resize(N+1);
        for(int i=1;i<=N;i++) cin >> arr[i];
        gredi = vector<vector<int> >(N+1, vector<int> (P+1));
        for(int i=1;i<=N;i++) {
            for(int j=1;j<=P;j++){
                cin >> gredi[i][j];
            }
            
            sort(gredi[i].begin()+1, gredi[i].end());
        }
        
        int s=1, ans= 0;
        while(1) {
            int cnt = 0;
            for(int i=1;i<=N;i++){
                for(int j=1;j<=P;j++) {
                    double last = gredi[i][j];
                    if(last <= 1.1*arr[i]*s && last >= 0.9*arr[i]*s){
                        cnt++;
                        break;
                    }
                }
            }

            if(cnt==N) {
                ans++;
                for(int i=1;i<=N;i++){
                    for(int j=1;j<=P;j++) {
                        double last = gredi[i][j];
                        if(last <= 1.1*arr[i]*s && last >= 0.9*arr[i]*s){
                            gredi[i][j] = -1;
                            break;
                        }
                    }
                }
            } else {
                s++;
            
                bool flag = false;
                for(int i=1;i<=N;i++) {
                    if(gredi[i].back() == -1) {
                        flag= true;
                        break;
                    }
                    double last = gredi[i].back();
                    if(last < 0.9*arr[i]*s) {
                        flag = true;
                        break;
                    }
                }
                if(flag) {
                    break;
                }
            }
        }
        
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
