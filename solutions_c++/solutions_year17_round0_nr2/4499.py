#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int test = 1;
    while(test <= t) {
        string s,res,s1;
        cin >> s;
        s1 = s;
        int len = s.length();
        res = "";
        int check = 0;
        for(int i = 0;i < s.length()-1 ; i++) {
            if(check == 0 && s[i] > s[i+1]) {
                char c = (char)(s[i]-1);
                s[i] = c;
                s[i+1] = '9';
                int j = i;
                while( j >= 1 && s[j-1] > s[j]) {
                    s[j] = '9';
                    char c = (char)(s[j-1]-1);
                    s[j-1] = c;
                    j--;
                }
                check = 1;
            }
            else if(check == 1) {
                s[i] = '9';
                s[i+1] = '9';
            }
        }
        if(s[0] == '0') {
            for(int i=1;i<s.length();i++) {
                res += s[i];
            }
        }
        else {
            res = s;
        }
        cout << "Case #" << test << ":" << " " << res  << endl;
        test++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

