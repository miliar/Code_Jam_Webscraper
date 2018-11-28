#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;
int last[1010];
bool tidy(int x){
    vector<int> s;
    while (x > 0){
        s.push_back(x % 10);
        x = x / 10;
    }
    for (int i = s.size() - 1; i > 0; i--){
        if (s[i] > s[i - 1]) return false;
    }
    return true;
}

int main(){
    ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    int n;
    last[1] = 1;
    for (int j = 2; j < 1002; j++){
        if (tidy(j)) last[j] = j;
        else last[j] = last[j - 1];
    }
    for (int i = 1; i <= T; i++){
        cin >> n;
        cout << "Case #" << i << ": " << last[n] << endl;   
    }
}
