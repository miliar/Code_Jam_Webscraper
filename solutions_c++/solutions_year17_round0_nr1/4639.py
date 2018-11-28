#include <bits/stdc++.h>

using namespace std;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int t;
    cin>>t;
    int rep(0);
    while (t--){
        bool ok=true;
        rep++;
        string  s;
        int k;
        cin>>s>>k;
            int cnt(0);
            for(int i(0);i<s.size();++i){
                if (s[i]=='-'){
                cnt++;
                if (i+k<=s.size()){
                for(int j(i);j<i+k;++j){
                        if (s[j]=='-'){
                            s[j]='+';
                        }
                       else  if (s[j]=='+'){
                            s[j]='-';
                        }
                    }

                    }}}

                    for(int i(0);i<s.size();++i){
                            if (s[i]=='-'){
                            ok=false;
                            break;


                            }


                    }





                    cout<<"Case #"<<rep<<": ";
                    if (ok==false){
                    cout<<"IMPOSSIBLE"<<endl;
                    }
                    else {

                        cout<<cnt<<endl;
                    }
                    }

    return 0;
}
