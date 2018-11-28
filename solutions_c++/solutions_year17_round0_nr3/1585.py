#include<iostream>
#include<cstdint>
#include<queue>

using namespace std;
typedef int64_t var;
var t, n, k;

int main(){
    cin >> t;
    for(var i = 0; i < t; ++i){
        cin >> n >> k;
        var npr = 1;
        var nb = 0;
        for(var j = 0; j < k;){
            n--;
            if(j+npr>=k){
                if(k>j+npr-nb){
                    n--;
                }
                var max = ((n/2)+(n&1));
                var min = n/2;
                cout << "Case #" << (i+1) << ": " << max << ' ' << min << endl;
                break;
            }else{
                var sp=n/2+(n&1);
                if(n&1){
                    nb=2*nb+(npr-nb);
                }
                j+=npr;
                n=sp;
                npr*=2;
            }
        }
    }
    return 0;
}
