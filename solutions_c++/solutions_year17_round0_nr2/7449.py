#include<iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(auto t = 1; t <= T; t++){
        long long N;
        cin >> N;
        int n[20];
        long long N1 = N;
        int k = 20;
        while(N1 > 0){
            n[--k] = N1%10;
            N1 /= 10;
        }
        int i;
        for(i = k+1; i < 20; i++){
            if(n[i-1] > n[i]){
                n[i-1]--;
                break;
            }
        }
        for(auto j = i; j < 20; j++)
            n[j] = 9;
        for(auto j = i-2; j >= k; j--){
            if(n[j] > n[j+1]){
                n[j]--;
                n[j+1] = n[j+2];
            }
        }
        while( (n[k] == 0) && (k< 20))
            k++;
//        for( auto j = k; j < 20; j++){
//            if(n[j] == 0)
//                k++;
//            else
//                break;
//        }
        cout << "Case #" << t << ": ";
        for(auto j = k; j < 20; j++)
            cout << n[j];
        cout << "\n";
    }
    return 0;
}
