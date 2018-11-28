#include <string>
#include <iostream>

using namespace std;

int main(){
    int T,n=0;
    
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> T;

    while(n<T){
        string input;
        int k;

        cin >> input >> k;

        int s=0,len=input.length();
        int ret=0;
        for(int i=0;i+k<=len;i++){
            if(input[i] == '-'){
                ret++;
                for(int j=i;j<i+k;j++){
                    if(input[j] == '+')input[j] = '-';
                    else input[j] = '+';
                }
            }
            //cout << i << ";" << input << "\n";
        }
        int cnt = 0;
        for(int i=0;i<len;i++){
            if(input[i] == '+')cnt++;
        }
        if(cnt == len)cout << "Case #" << n+1 << ":" << " " << ret << "\n";
        else cout << "Case #" << n+1 << ":" << " " <<"IMPOSSIBLE" << "\n";
        n++;
    }

    return 0;
}