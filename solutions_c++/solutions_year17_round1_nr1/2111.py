
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;


char arr[30][30];

int r,c;




int main(){


    int t;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){


        cin >> r >> c;

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin >> arr[i][j];
            }
        }

        int fchare = 0;
        for(int i=0;i<r;i++){
            char wasc = '?';
            for(int j=0;j<c;j++){
                if(arr[i][j] != '?'){
                    wasc = arr[i][j];
                    int k;
                    if(j > 0)
                        for(k=j-1;k>=0;k--){
                            if(arr[i][k] == '?')
                                arr[i][k] = wasc;
                            else
                                break;
                        }
                    for(k=j+1;j<c;j++){
                        if(arr[i][k] == '?')
                            arr[i][k] = wasc;
                        else
                            break;
                    }
                    j = k-1;
                }
            }
            if(wasc == '?'){
                if(i == fchare){
                    fchare++;
                }
                else{
                    for(int h=0;h<c;h++){
                        arr[i][h] = arr[i-1][h];
                    }
                }
            }
        }
        if(fchare > 0){
            for(int g = 0;g<fchare;g++){
                for(int h=0;h<c;h++){
                    arr[g][h] = arr[fchare][h];
                }
            }
        }


        cout << "Case #" << tt << ":" << endl;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout << arr[i][j];
            }
        cout << endl;
        }

    }

    return 0;

}
