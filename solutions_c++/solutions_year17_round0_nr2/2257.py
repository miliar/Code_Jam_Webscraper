#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string test()
{
    string s;
    cin >> s;
    if(s.size()==1)return s;
    string t = "";
    for(int i=0;i<s.size();i++)
    {
        if(i>0 && s[i]-'0' < s[i-1]-'0')
            break;
        if(i==s.size()-1) return s;
        int prev = 0;
        if(i>0) prev = s[i-1]-'0';
        if(prev >= s[i]-'0')
            continue;
        string k = "";
        for(int j=0;j<i;j++)
            k += s[j];
        k += (char)(s[i]-'0'-1+'0');
        for(int j=i+1;j<s.size();j++)
            k += '9';
        t = k;
    }
    string ans = "";
    int v = 0;
    while(t[v] =='0') v++;
    for(;v<s.size();v++)
        ans += t[v];
    return ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        string a = test();
        cout << "Case #" << i+1 << ": " << a << '\n';
    }
    return 0;
}