#include <bits/stdc++.h>
using namespace std;

#define ll long long
int arr[30];
int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    scanf("%d"  , &t);
    int alp = 1;
    while(t--){
        string str;
        cin >> str;
        int n = str.length();

        for(int i = 0 ; i < 30 ; i++){
            arr[i] = 0;
        }
        for(int i = 0 ; i < n ; i++){
            arr[i] = str[i] - '0';
        }

        while(1){
            int o = 0;
            int hi = 0;
            for(int i = 0 ; i < n ; i++){
                if(arr[i] >= hi){
                    hi = arr[i];
                }
                else{
                    //cout<"here "<<str[i]<<endl;
                    o = 1;
                    arr[i - 1]--;
                    //cout<<"here "<<str[i - 1]<<"   "<<str[i]<<endl;
                    for(int j = i ; j < n ; j++){
                        arr[j] = 9;
                    }
                    break;
                }
            }
            if(o == 0) break;
        }
        int i = 0;
        while(arr[i] == 0) i++;
        printf("Case #%d: " , alp);
        for(int j = i ; i<n; i++){
            printf("%d" , arr[i]);
        }
        if(t == 0) break;
        printf("\n");
        alp++;
    }


}
