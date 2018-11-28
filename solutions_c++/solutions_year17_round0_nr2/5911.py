#include<iostream>
#include<vector>

typedef long long int lli;

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int itrS = 1; itrS <= t; itrS++){
        lli n;
        cin >> n;
        vector<int> d;
        while(n){
            d.push_back(n % 10);
            n /= 10;
        }
        int ref = -1;
        for(int i = 0; i < d.size() - 1; i++){
            if(d[i] < d[i + 1]){
                ref = i + 1;
                d[i + 1]--;
            }
        }
        for(int i = 0; i < ref; i++)
            d[i] = 9;
        for(int i = d.size() - 1; i >= 0; i--)
            n = n * 10 + d[i];
        cout << "Case #" << itrS << ": "<< n << "\n";
    }
    return 0;
}
