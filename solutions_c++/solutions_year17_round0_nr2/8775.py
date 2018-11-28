#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t,ca=0;
    freopen("br.in","r",stdin);
    freopen("out.txt","w",stdout);
     long long n;
    cin>>t;
    while(t--){
            ca++;
        cin>>n;
        for( long long i=n;i>=0;i--){
            stringstream ss;
            ss << i;
            string str = ss.str();
            string s=str;
            sort(str.begin(),str.end());
            if(s==str) {
                cout<<"Case #"<<ca<<": "<<s<<endl;
                break;
            }
        }

    }
    return 0;
}
