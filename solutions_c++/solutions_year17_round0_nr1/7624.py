// author - vanshaj2608 jaypee institute of information technology.
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    freopen("codejaminput1.txt" , "r" , stdin);
    freopen("codejamoutput1.txt" , "w" , stdout);

    cin>>t;
    for(int test=1;test<=t;test++)
    {
        string s;
        cin>>s;
        int k ;
        cin>>k;
        int ans=0;
        int len = s.length();
        for(int i=0;i<=len-k;i++)
        {
                if(s[i] == '-')
                {
                    ans++;
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j] == '-'){
                            s[j] = '+';
                        }
                        else s[j] = '-';
                    }
                }
        }
        bool found=false;
        for(int i=0;i<len;i++)
        {
            if(s[i] == '-')
                {
                    found=true;
                }
        }
         cout << "Case #" <<test<<": ";
        if(found){
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout<<ans<<endl;
        }
    }
    return 0;
}
