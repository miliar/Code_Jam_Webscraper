#include <iostream>
using namespace std;
int main() {
    int T, cnt = 1;
    cin >> T;
    int ans;
    while(T) {
        int N;
        ans = 0;
        cin >> N;
        if( N < 10) {
            ans = N;
        } else if (N >=10 && N<100) {
            for(int i=1; i<=N; i++) {
                if(i/10 <= i%10)
                    ans = i;
            }
        } else if (N >= 100 && N < 111) {
            ans = 99;
        } else if (N >= 111 && N <= 999) {
            for(int i=111; i<=N;i++) {
                if(((i%10)>=((i/10)%10)) && (((i/10)%10)>=(i/100)))
                    ans = i;
            }
        
        } else if (N==1000) {
            ans = 999;
        }
        
        cout << "Case #" << cnt << ": " << ans << endl;
        cnt++;
        T--;
    }
    
}