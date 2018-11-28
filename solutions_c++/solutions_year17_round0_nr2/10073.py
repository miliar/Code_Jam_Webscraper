#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    long long int tmp,tmpK,mx,keta=1;
    cin >> n;
    long long int ar[n];
    for(int i=0; i<n; i++){
        cin >> tmp;
        ar[i] = tmp;
        if(tmp<=11){
            continue;
        }

        mx = tmp%10;
        if(mx == 0) {
            ar[i] = tmp-1;
            tmp = ar[i];
            mx = 9;
        }
        re:
        tmp /= 10;
        keta = 1;
        while(tmp!=0){
            tmpK = tmp%10;
            if(tmpK>mx){
                if(keta != 1){
                    ar[i] -= (ar[i]%(keta/10)) +1;
                    tmp = ar[i];
                }else {
                    ar[i] -= (mx + 1);
                }
                tmp = ar[i];
                mx = tmp%10;
                goto re;
            }else {
                mx = tmpK;
            }
            tmp /= 10;
            keta*=10;
        }
    }
    for(int i=0; i<n; i++){
        cout << "Case #"<< i+1 <<": "<<ar[i]<<endl;
    }
    return 0;
}