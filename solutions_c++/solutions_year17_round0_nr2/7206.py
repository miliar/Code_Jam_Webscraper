// tidy
#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int main(){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i ++){
        string strx;
        char prev;
        cin >> strx;

        prev = strx[0];
        int j;

        for(j = 1; j < strx.size(); j++){
            if(int(prev) > int(strx[j])){
                strx[j-1] = int(strx[j-1]) - 1;
                for(int k = j - 1; k > 0; k--){
                    if(int(strx[k - 1]) > int(strx[k])){
                        strx[k-1] = strx[k-1] - 1;
                        j--;
                    }
                    else
                        break;
                }
                break;
            }
            prev = strx[j];
        }

        if(j == 1 && strx[j-1] == '0')
            strx[j-1] = 0;
        for(;j <= strx.size(); j++){
            strx[j] = '9';
        }

        cout << "Case #" << i << ": " ;
        if(strx[0] != 0)
            cout << strx[0];

        for(int j = 1; j < strx.size(); j ++){
            cout << strx[j];
        }
        cout << endl;
    }
}
