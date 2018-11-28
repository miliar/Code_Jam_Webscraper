#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-Output.out","w",stdout);
    int t;
    string s;
    cin >> t;
    for (int loop=1;loop<=t;loop++)
    {
        cin >> s;
        for (int i=0;i< s.size()-1; i++){
            if (s[i]-'0' > s[i+1]-'0'){
                //cout << "Inside";
                while (s[i]==s[i-1]) i--;
                //cout <<" "<<i;
                s[i] = ((s[i]-'0')-1)+'0';
                //cout <<" "<<s[i];
                for (int j=i+1;j<s.size();j++){
                    s[j]='9';
                }
                //cout <<" "<<s<<endl;
                break;
            }
        }
        cout << "Case #"<<loop<<": ";
        for (int i=0;i<s.size();i++){
            if (s[i]!='0') cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
