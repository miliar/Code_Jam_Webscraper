#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

vector<int> get_dig(int a) {
    vector<int> dig;
    int d = log10(a);
    int temp;
    for (int i = 0; i <= d; i++) {
        temp = a % 10;
        dig.push_back(temp);
        a = (a - temp) / 10;
    }
    return dig;
}

bool isTidy(int N){
    vector<int> dig = get_dig(N);
    for(int i=0; i<dig.size()-1; i++){
        if(dig[i] < dig[i+1]) return false;
    }
    return true;
}

int solve(int N){
    while(true){
        if(isTidy(N)) return N;
        N--;
    }
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        cout << "Case #" << i+1 << ": ";
        cout << solve(N) << endl;
    }

    return 0;
}
