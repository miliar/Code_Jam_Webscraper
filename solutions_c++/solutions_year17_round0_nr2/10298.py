#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for(int i = 1 ; i <= t; ++i){
        long N,res;
        cin >> N;
        //Brute Force
        for(long j = N; j >= 1; --j){
            long jj = j; int start = jj % 10;
            jj /= 10;
            while(jj){
                int curr = jj % 10;
                if(curr > start) break;
                start = curr;
                jj /= 10;
            }
            if(!jj){
                res = j;
                break;
            }
        }

        cout << "Case #" << to_string(i) << ": " << to_string(res) << endl;


    }

    return 0;
}
