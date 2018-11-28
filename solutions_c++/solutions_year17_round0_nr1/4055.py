#include <iostream>
using namespace std;

int main() {
    
    freopen("cjinput.txt", "r", stdin);
    freopen("cjoutput.txt", "w", stdout);

    int t;
    cin>>t;
    string s;
    int n,k,ans;
    for(int j=1;j<=t;j++) {
        cin>>s>>k;
        ans=0;
        n=s.length();

        while(true) {

            int pos=n-1;
            while(pos>=0&&s[pos]=='+') {
                pos--;
            }
            if(pos<0 || pos+1<k) {
                break;
            }
            for(int i=0;i<k;i++) {

                s[pos-i]=='+'?s[pos-i]='-':s[pos-i]='+';
            }
            ans++;

        }
        int cn=0;
        for(int i=0;i<n;i++) {
            if(s[i]=='+')
                cn++;
        }
        cout<<"Case #"<<j<<": ";
        if(cn==n) {
            cout<<ans<<endl;
        }else {
            cout<<"IMPOSSIBLE\n";
        }
 




    }

    return 0;
}