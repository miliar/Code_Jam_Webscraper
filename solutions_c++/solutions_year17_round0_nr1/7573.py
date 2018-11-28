#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int k;
        string str;
        cin>>str>>k;
        int ans = 0;
        
        for(int j=0; j<=str.length()-k; j++)
        {   
            if(str[j] == '-')
            {
                for(int l=0; l<k; l++)
                {
                    if(str[j+l] == '-')
                        str[j+l] = '+';
                    else
                        str[j+l] = '-';
                }
                ans++;
            }
        }
        
        bool flag = true;
        for(int j=0; j<str.length(); j++)
            if(str[j] == '-')
            {
                flag = false;
                break;
            }
        
        cout<<"Case #"<<i<<": ";
        if(flag)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
