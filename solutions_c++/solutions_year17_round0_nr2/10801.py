#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    int q;
    cin >> q;
    for(int t = 0; t < q; t++){
        unsigned long long n;
        cin >> n;
        unsigned long long temp;
        int old_temp = n%10;
        int new_temp = n%10;
        while(n){
            int flag = 0;
            temp = n;
            old_temp = temp%10;
            while(temp){
                new_temp = temp%10;
                temp = temp/10;
                if(old_temp < new_temp){
                    flag = 1;
                    break;
                }
                old_temp = new_temp;
            }
            if(flag == 0){
                break;
            }
            n--;
        }
        cout << "Case #" << t+1 << ": "<< n << '\n';
    }
    return 0;
}
