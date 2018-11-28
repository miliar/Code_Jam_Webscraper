#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    cin >> T;
    while(T--)
    {
        cout << "Case #" << ++cas << ": ";
        string str;
        int K;
        cin >> str >> K;
        int ans=0;
        for(int i=0;i<=str.size()-K;i++)
        {
            if(str[i]=='-')
            {
                ++ans;
                for(int j=0;j<K;++j)
                    if(str[i+j]=='-') str[i+j]='+';
                    else str[i+j]='-';
            }
        }
        int flag=0;
        for(int i=str.size()-K;i<str.size();++i)
        if(str[i]=='-') {flag=1;break;}
        if(flag) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
