#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>             
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int cases;
    cin >> cases;
    bool p[1010];

    for(int tt = 1;tt <= cases;tt++){

        int k;
        string pancakes;
        cin >> pancakes >> k;

        int n = (int)pancakes.size();

        for(int i = 0;i < n;i++) p[i] = (pancakes[i]=='+');

        int inv = 0;
        for(int i = 0;i < n-k+1;i++){
            
            if(p[i]) continue;

            inv++;
            for(int j = 0;j < k;j++) p[i+j] ^= 1;
        }   
        
        bool shit = false;
        for(int i = 0;i < n;i++) if(!p[i]) shit = true;

        cout << "Case #" << tt << ": ";
        if(shit) cout << "IMPOSSIBLE" << endl;
        else cout << inv << endl; 

    }

    return 0;
}
