
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;




int main(){

    int t;
    cin >> t;
    for(int tt = 1;tt<=t;tt++){

        string s;
        cin >> s;

        int len = s.length();

        int arr[25];

        for(int i=0;i<len;i++){
            arr[i] = s[i]-'0';
        }

        for(int i=len-1;i>0;i--){
            if(arr[i] < arr[i-1]){
                arr[i-1]--;
                for(int j=i;j<len;j++)
                    arr[j] = 9;
            }
        }

        int wn = 0;
        cout << "Case #"<<tt<<": ";
        for(int i=0;i<len;i++){
            if(!arr[i] && !wn)
                continue;
            wn = 1;
            cout << arr[i];
        }
        cout << endl;
    }
    return 0;
}
