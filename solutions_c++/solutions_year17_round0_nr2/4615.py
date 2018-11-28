#include <bits/stdc++.h>

using namespace std;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    int rep=0;
    while (t--)
    {
        rep++;
        long long int n;
        string s;
        bool ok=true;
        cin>>s;
        for(int i(0); i<s.size()-1; ++i)
        {
            if (s[i]>s[i+1])
            {
                ok=false;
                break;
            }

        }
        if (ok)
        {
            cout<<"Case #"<<rep<<": ";
            cout<<s<<endl;
            continue;
        }
        else
        {

            int pos=0;
                while (s[pos]<=s[pos+1] && pos<s.size()-1){
                    pos++;
                }
                    char k=s[pos];
                    while (s[pos]==k && pos>0){
                    pos--;
                    }
                    if (pos==0){
                        if (s[0]!=k){
                                pos++;
                                s[pos]=((s[pos]-'0')-1)+'0';
                        for(int i(pos+1);i<s.size();++i)
                        {
                        s[i]='9';
                        }
                        }
                        else{
                            s[pos]=((s[pos]-'0')-1)+'0';
                        for(int i(pos+1);i<s.size();++i)
                        {
                            s[i]='9';
                        }



                        }
                    } else {
                        pos++;
                        s[pos]=((s[pos]-'0')-1)+'0';
                        for(int i(pos+1);i<s.size();++i)
                        {
                        s[i]='9';
                        }




                    }

                    int i(0);
                    while (s[i]=='0'){
                    i++;
                    }
                    cout<<"Case #"<<rep<<": ";
                    for(int j(i);j<s.size();j++){
                    cout<<s[j];
                    }
                    }
                    cout<<endl;
                    }











    return 0;
}
