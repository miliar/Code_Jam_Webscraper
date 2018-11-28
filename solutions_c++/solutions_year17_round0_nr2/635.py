#include <iostream>
#include <cstdio>
#include <vector>
#define ll long long

using namespace std;

int T;
string N;

int main(){
    freopen("data2.in","r",stdin);
    freopen("data2.out","w",stdout);
    cin >> T;
    for (int z = 1; z <= T; z++){
        cin >> N;
        for (int i = (int)N.length()-1; i; i--){
            if (N[i] < N[i-1]){
                for (int j = i; j < N.length(); j++) N[j] = '9';
                N[i-1]--;
            }
        }
        while(N[0] == '0') N = N.substr(1);
        printf("Case #%d: %s\n",z,N.c_str());
    }
    return 0;
}
