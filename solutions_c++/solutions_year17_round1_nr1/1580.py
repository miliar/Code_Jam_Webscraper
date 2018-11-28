#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

bool needs(string* arr, int R, int C){
    for(int r = 0 ; r < R ; r++){
        for(int c = 0 ; c < C ; c++){
            if(arr[r][c] == '?'){
                return true;

            }

        }

    }

return false;
}

int main(){
	int testCases;
    cin >> testCases;
    
    string arr[25];
    for(int t = 1 ; t <= testCases ; t++){
        int R;
        int C;
        cin >> R;
        cin >> C;
        
        cin.ignore(256, '\n');


        for(int i = 0 ; i < R ; i++){
            getline(cin, arr[i]);
        }

        /*
        printf("Case #%d:\n", t);
        for(int r = 0 ; r < R ; r++){
            cout << arr[r]<<endl;
        }
        continue;

        */

        for(int r = 0 ; r < R ; r++){
            for(int c = 0; c < C ; c++){
                if(arr[r][c] == '?'){
                    continue;
                }

                char target = arr[r][c];
                for(int x = c - 1 ; x >= 0 ; x--){
                    if(arr[r][x] != '?'){
                        break;
                    }
                    arr[r][x] = target;
                }

                for(int x = c + 1 ; x < C ; x++){
                    if(arr[r][x] != '?'){
                        break;
                    }
                    arr[r][x] = target;
                }


            }
        }

        while(needs(arr,R, C)){
            for(int r = 0; r < R ; r++){
                for(int c = 0 ; c < C ; c++){
                    if(arr[r][c] == '?'){
                        if(r == 0){
                            arr[r][c] = arr[r+1][c];
                        }else if(r == R-1){
                            arr[r][c] = arr[r - 1][c];
                        }else{
                            if(arr[r-1][c] != '?'){
                                arr[r][c] = arr[r-1][c];
                            }else{
                                arr[r][c] = arr[r+1][c];

                            }

                        }
                    }
                }

            }

        }


        printf("Case #%d:\n", t);
        for(int r = 0 ; r < R ; r++){
            cout << arr[r]<<endl;
        }


        

    }

}

