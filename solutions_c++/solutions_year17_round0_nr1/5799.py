#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("res.txt","w",stdout);
    int t;
    int c=0;
    cin>>t;
    while(t--){
        c++;
        string s;
        cin>>s;
        int k;
        cin>>k;
        int nb=0;
        for(int i=0;i<s.length()-k+1;++i){
            if(s[i]=='-'){
                for(int j=0;j<k;++j){
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
                nb++;
            }
        }
        int i;
        for(i=0;i<s.length();++i){
            if(s[i]=='-'){
                cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
                break;
            }
        }
        if(i==s.length())
            cout<<"Case #"<<c<<": "<<nb<<endl;
    }
    return 0;
}
