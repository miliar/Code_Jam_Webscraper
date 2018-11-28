#include <bits/stdc++.h>
using namespace std;
int ans1;
int ans2;
void solve(vector<int> &arr){
    int n = arr.size();
    int best = 0;
    pair<int,int> var;
    pair<int,int> prev;
    prev.first = 0;
    prev.second = 0;
    for(int i = 0 ; i < n ; i++){
        if(arr[i] == 1)
            continue;
        var.first = 0;
        var.second = 0;
        for(int j = i-1 ; j >= 0 ; j-- ){
            if(arr[j] == 1)
                break;
            if(arr[j] == 0)
                var.first +=1;
        }
        for(int j = i+1 ; j < n ; j++){
            if(arr[j] == 1)
                break;
            if(arr[j] == 0)
                var.second += 1;
        }
        int x = min(var.first , var.second);
        int y = min(prev.first , prev.second);
        if(x > y){
            best = i;
            prev.first = var.first;
            prev.second = var.second;
        }else if(x == y){
            if(var.first >= prev.first){
                best = i;
                prev.first = var.first;
                prev.second = var.second;
            }
        }
    }
    ans1 = prev.first;
    ans2 = prev.second;
    arr[best] = 1;

}
int main(){
    freopen("in.txt" , "r" ,  stdin);
    freopen("out.txt" , "w" , stdout);
    int tc;
    scanf("%d" , &tc);
    for(int i = 1 ; i <= tc; i++){
        int n , k;
        scanf("%d%d" , &n , &k);
        vector<int> arr(n, 0);
        ans1 = 0;
        ans2 = 0;
        while(k--){
            solve(arr);
        }
        cout << "Case #" << i << ": ";
        cout << ans1 << " " << ans2 << "\n";

    }


}
