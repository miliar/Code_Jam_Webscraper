#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <list>
#include <cmath>
#include <string>

using namespace std;
typedef long long lli;

int main(){
    ofstream aout ( "a_out.txt" );
    lli t;
    cin>>t;
    lli cnt=1;
    while(t--)
    {
        lli k;
        string s;
        cin>>s;
        cin>>k;
        lli ans=0;
        bool flag=false;
        for(lli i = 0; i<=s.length()-k; i++){
            if(s[i]=='-')
            {
                ans++;
                for(lli j=i;j<k+i;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
//            cout <<i<<" "<<s[i]<<endl;
//            cout <<i<<" "<<s[i]<<endl;
//            cout<<s<<"*"<<endl;
        }
        cout<<"Case #"<<cnt<<": ";
        aout<<"Case #"<<cnt<<": ";
        for(lli i = (lli)s.length()-1 ; i>=((lli)s.length()-k) ;i--){
//                cout <<i<<" "<<s[i]<<endl;
            if(s[i]=='-'){
                cout<<"IMPOSSIBLE\n";
                aout<<"IMPOSSIBLE\n";
                flag=true;
                break;
            }
        }
        if(!flag){
            cout<<ans<<endl;
            aout<<ans<<endl;
        }
        cnt++;
    }
}

