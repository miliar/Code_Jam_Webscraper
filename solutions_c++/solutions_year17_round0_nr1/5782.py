#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,test=1;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int k;
        cin >> k;
        int counter = 0;
        for(int i=0;i<=s.length()-k;i++){
            if(s[i] == '-'){
                for(int j=i;j<i+k;j++){
                    if(s[j] == '-')s[j] = '+';
                    else s[j] = '-';
                }
                counter++;
            }
            //cout << s << endl;
        }
        for(int g=0;g<s.length();g++){
            if(s[g] == '-'){
                cout << "Case #" << test << ": ";
                cout << "IMPOSSIBLE\n";
                goto label;
            }
        }
        cout << "Case #" << test << ": ";
        cout << counter << endl;
        label:;
        test++;
    }
    return 0;
}
