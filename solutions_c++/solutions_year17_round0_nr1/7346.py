#include <iostream>
using namespace std;

char flip(char s)
{
    if(s=='-')
        return '+';
    return '-';
}
int main()
{
    int t,x=1;
    cin>>t;
    while(t--)
    {
        bool ans = true;
        string s;
        int k,count = 0;
        cin>>s>>k;
        for(int i = 0;i <=s.size()-k; i++)
        {
            if(s[i]=='-')
            {
                for(int j = 0; j<k;j++)
                {
                    s[i+j] = flip(s[i+j]);
                }
                count++;
            }
        }
        for(int i= s.size()-1; i >= s.size()-k && i>= 0;i--)
        {
            if(s[i] =='-')
                ans = false;
        }
        cout<<"Case #"<<x++<<": ";
        if(ans)
        cout<<count<<endl;
        else
        cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
