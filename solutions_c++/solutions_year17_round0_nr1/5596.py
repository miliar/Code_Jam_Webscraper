#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int t, k, pos, ans, flag = 0;
    string s, q;
    cin>>t;
    for(int x=0; x<t; ++x){
        cin>>s>>k;
        ans=0;
        flag=0;
        pos = s.find('-');
        while(pos!=string::npos)
        {
            if(pos > s.size() - k){
                cout<<"Case #"<< x+1 << ": IMPOSSIBLE\n";
                flag = 1;
                break;
            }
            for(int i=0, sz=s.size(); i<k; ++i){
                if(s[i+pos]=='+')
                    s[i+pos]='-';
                else
                    s[i+pos]='+';
            }
            ans++;
//            cerr<<s<<endl;
            pos = s.find('-');
        }
        if(flag==0)
            cout<<"Case #"<< x+1 << ": " << ans << endl;
    }
    return 0;
}
