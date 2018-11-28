#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <list>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T, K;
    cin>>T;
    int count = 0;
    while(T--) {
        count++;
        cout<<"Case #"<<count<<": ";
        string pancakes;
        cin>>pancakes;
        cin>>K;
        int num_flips = 0;
        bool impossible = false;
        for(int i = 0; i < pancakes.size(); i++) {
            if(pancakes[i] == '-') {
                // Need to flip
                num_flips += 1;
                if(i+K > pancakes.size()) {
                    // If we can't flip, it's impossible to solve
                    cout<<"IMPOSSIBLE\n";
                    impossible = true;
                    break;
                }
                for(int j = i; j < i+K; j++) {
                    if(pancakes[j] == '-') {
                        pancakes[j] = '+';
                    } else {
                        pancakes[j] = '-';
                    }
                }
            }
        }
        if(!impossible) {
            cout<<num_flips<<"\n";
        }
        if(T < 0) {
            break;
        }
    }
    return 0;
}