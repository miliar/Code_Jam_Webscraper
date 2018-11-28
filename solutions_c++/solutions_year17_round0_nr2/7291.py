#include <iostream>
//B-large
using namespace std;

int main(){
    int T,n=0;

    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> T;

    while(n<T){
        long long N;
        int k[19]={0};

        cin >> N;

        long long hoge = N;

        int dcnt=0;

        while(hoge){
            hoge /= 10;
            dcnt++;
        }

        hoge = N;
        for(int i=0;i<dcnt;i++){
            k[i] = hoge%10;
            hoge /= 10;
        }
        ret:
        for(int i=dcnt-1;i>0;i--){
            if(k[i] == 0)continue;

            if(k[i] > k[i-1]){
                k[i]--;
                for(int j=i-1;j>=0;j--)k[j] = 9;
            } 
        }

        for(int i=dcnt-1;i>0;i--)if(k[i] > k[i-1])goto ret;

        cout << "Case #" << n+1 << ":" << " " << "\0";
        for(int i=dcnt-1;i>=0;i--){
            if(k[i] == 0)continue;

            cout << k[i] << "\0";
        }
        cout << "\n";
        n++;
    }

    return 0;
}