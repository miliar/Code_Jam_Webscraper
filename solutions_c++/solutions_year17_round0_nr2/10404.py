#include <bits/stdc++.h>

using namespace std;
bool cek (long long x){
    long long besaran = 100000;
    while(x/besaran==0){
        besaran = besaran / 10;
    }besaran = besaran*10;
    long long tmp1, tmp2, tmp3;
    tmp1 = 0;
    while(besaran>0){
        tmp3 = tmp1;
        tmp1 = (x / besaran)%10;
        tmp2 = tmp3;
        if(tmp1<tmp2){
            return false;
        }
        besaran = besaran / 10;
    }
    tmp1 = x%10;
    tmp2 = (x/10)%10;
    if(tmp1<tmp2) return false;
    else return true;
}
int main()
{
    long long T, input;
    cin >> T;
    for(long long t = 0;t<T;t++){
            cin >> input;
        for(long long x = input;x>0;x--){
            if(cek(x)) {
                cout <<"Case #"<<t+1<<": "<<x << endl;
                break;
            }
        }
    }
    return 0;
}
