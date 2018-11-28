
#include <bits/stdc++.h>

using namespace std;


typedef long long int ll;




int main(){


    int t;

    cin >> t;




    for(int tt = 1;tt<=t;tt++){
        int arr[1005];
        string s;
        int k;
        cin >> s >> k;
        int cc = 0;
        int len = s.length();

        for(int i=0;i<s.length();i++){
            if(s[i] == '+')
                arr[i] = 1;
            else
                arr[i] = 0;
        }

        int br = 0;
        for(int i=0;i<len;i++){

            if(!arr[i]){

                if(i+k > len){
                    br = 1;
                    break;
                }

                cc++;
                for(int j=0;j<k;j++){

                    arr[i+j] = 1-arr[i+j];

                }

            }

        }

        if(br){
            cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
        }
        else{
            cout << "Case #" << tt << ": " << cc << endl;
        }

    }

    return 0;

}
