#include <iostream>

using namespace std;

int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        string s;
        int n;
        cin>>s>>n;
        int ans=0;

        for (int i=0;i<=s.length()-n;i++){
            if (s[i]=='-'){
                for (int j=i;j<i+n;j++)
                    s[j]=(s[j]=='-')?'+':'-';
                ans++;
            }
        }
        bool impossible=false;
        for (int i=0;i<s.length();i++){
            if (s[i]=='-'){
                impossible=true;
                break;
            }
        }
        if (impossible)
            cout<<"Case #"<<(test+1)<<": Impossible"<<endl;
        else
            cout<<"Case #"<<(test+1)<<": "<<ans<<endl;
    }




}
