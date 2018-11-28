#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isTidy(long long n)
{
    string s = to_string(n);
    for(int i = 0 ; i < int(s.length())-1 ; i++)
    {
        if(s[i] > s[i+1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int n;
    long long m;
    cin >>n;
    for(int i=1;i<=n;i++)
    {
        cin >> m;
        string s = to_string(m),c="";
        /*if(s[s.length()-1] == '0')
        {
            s[s.length()-1]='9';
            for(int j=0;j<int(s.length())-1;j++)
            {
                int t = int(s[j])-48;
                if(t>1)
                {
                    s[j]=char(t-1)+48;
                }
            }
            c = s;
            m = stoll(c.c_str());
        }*/
        while(!isTidy(m))
        {
            m--;
        }
        cout<< "Case #"+to_string(i)+": "+to_string(m)<<endl;
    }
    return 0;
}
