#include <bits/stdc++.h>
#include "bigint.h"
using namespace std;


bool isTidy(int *arr){
    int preDigit = arr[0],i=1;
    while(arr[i]!=-1){
        if(preDigit>arr[i]){
            return false;
        }
        preDigit = arr[i];
        i++;
    }
    return true;
}

int main()
{
    unsigned int t,i;
    cin >> t;

    int n[19];
    char ch;
    getchar();
    for(i=0;i<t;i++){
        cout << "Case #"<<(i+1)<<": ";
        int counter = 0;
        ch = getchar();
        while( ch != '\n' && ch != '\0'){
            n[counter] = ch - '0';
            ch = getchar();
            counter++;
        }
        n[counter] = -1;

        int j = 0;
        while(!isTidy(n)){
            int preDigit = n[0];
            for(j = 1; j < counter; j++){
                if(preDigit>n[j]){
                    n[j-1]--;
                    for(int k = j; k < counter; k++){
                        n[k] = 9;
                    }
                    break;
                }
                preDigit = n[j];
            }
        }

        bool bPreZero = n[0] == 0 ? true : false;
        for(j = 0; j < counter; j++){
            if(bPreZero){
                if(n[j] != 0){
                    cout << n[j];
                    bPreZero = false;
                }
            }
            else{
                cout << n[j];
            }
        }
        cout << endl;
    }
    return 0;
}
