#include <iostream>

using namespace std;

int main()
{
    freopen("C:\\Users\\Bibin\\Downloads\\C-large.in", "r", stdin);
    freopen("C:\\Users\\Bibin\\Downloads\\output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        long long N, K;
        cin >> N >> K;

        while( K > 1){
            if(N%2 == 0){
                N = (N-1)/2;
                if(K%2 == 0){
                    N++;
                }
            }else{
                N = N/2;
            }
            K = K/2;
        }
        cout << "Case #"<<t<<": "<< N/2 << " " << (N-1)/2 << "\n";
    }
}
