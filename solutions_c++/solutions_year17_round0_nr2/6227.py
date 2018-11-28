#include <bits/stdc++.h>

using namespace std;
string arr;
int n, k;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int t = 1;
    cin >> T;
    while(T--){
        cout << "Case #"<<t<<": ";

        cin >> arr;
        int mn = -1;
        for(int i = 0 ; i < arr.size() && mn == -1 ; i ++){
            for(int j = 0 ; j < i ; j++){
                if(arr[i] < arr[j] ){
                    mn = i;
                    break;
                }
            }
        }
        if(mn != -1){
            while(mn > 0 ){
                bool flag = false;
                for(int i = 0 ; i < mn ; i++){
                    if(arr[i] >= arr[mn]){
                        flag = true;
                        break;
                    }
                }
                if(!flag)break;
                mn--;
            }
            arr[mn]--;
            for(int i = mn+1 ; i < arr.size() ; i++){
                arr[i] = '9';
            }
            if(arr[0] == '0' && arr.size() > 0)
                arr = arr.substr(1);
        }
        cout << arr;
        cout << endl;
        t++;
    }
    return 0;
}
