#include <iostream>
#include <string>
using namespace std;


int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string n;
        cin >> n;
        n+="9";

        string ans=n;
        for (int i = n.size() - 2; i >= 0; i--)
        {
            if((int)n[i] > (int)ans[i+1])
            {
                ans[i] = n[i] - 1;
                for(int j=i+1;j<n.size()-1;j++)
                    ans[j] = '9';
            }
            else
            {
                ans[i] = n[i];
            }
        }

        cout<<"Case #";
        cout<<tt;
        cout<<": ";

        bool flag = false;
        for(int i=0;i<ans.size()-1;i++)
        {
            if(ans[i]!='0')
                flag=true;
            if(flag==false && ans[i]=='0')
                continue;
            cout<<ans[i];
        }
        cout<<endl;
    }
}