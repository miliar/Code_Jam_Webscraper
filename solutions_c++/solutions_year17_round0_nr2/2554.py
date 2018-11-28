#include <iostream>

using namespace std;

int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        string s;
        cin>>s;
        while (true){
            bool ok=true;
            for (int i=0;i<s.length()-1;i++){
                if (s[i]>s[i+1]){
                    ok=false;
                    if (i==0&&s[i]=='1'){
                        s.erase(0,1);
                        for (int j=0;j<s.length();j++){
                            s[j]='9';
                        }
                        break;
                    }
                    s[i]=s[i]-1;
                    for (int j=i+1;j<s.length();j++)
                    {
                        s[j]='9';
                    }
                    break;
                }
            }
            if (ok) break;
        }

            cout<<"Case #"<<(test+1)<<": "<<s<<endl;
    }




}
