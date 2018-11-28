#include <bits/stdc++.h>
#include <string>

using namespace std;


int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

   int T;
   string s;

   cin >> T;
   for(int i = 0; i < T; i ++) {
        cin >> s;
        int pos = s.length();
        for(int j = s.length() - 1; j >= 1; j--){
            int currentNum = s[j] - '0';
            int preNum = s[j-1] - '0';
            if(currentNum < preNum ){
                s[j-1] = s[j-1] - 1;
                pos = j;
            }
        }

        for(;pos < s.length(); pos++){
            s[pos] = '9';
        }

        long long result = 0;
        for(int j = 0; j < s.length(); j++){
            result = result*10 + s[j] - '0';
        }
        cout << "Case #" << i+1 << ": " << result << endl;
   }

    return 0;
}
