#include <bits/stdc++.h>

using namespace std;

long long stoi(string s)
{
    long long num=0;
    for (int i=0;i<s.size();i++)
    {
        num*=10;
        num+=s[i]-'0';
    }
    return num;
}

string res(string num)
{
    string tempRes;
    for (int i=0;i<num.size();i++) tempRes+='1';
    if (stoi(num)<stoi(tempRes)) return "";
    for (int i=0;i<num.size();i++)
    {
        for (char dig=((i>0)?tempRes[i-1]:'1');dig<='9';dig++)
        {
            string temp = tempRes;
            for (int j=i;j<num.size();j++)
                temp[j]=dig;
            if (stoi(temp)<=stoi(num)) tempRes=temp;
        }
    }
    return tempRes;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    //freopen("in.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int q=1;q<=t;q++)
    {
        cout<<"Case #"<<q<<": ";
        string s;
        cin>>s;
        string curRes;
        for (int i=0;i<s.size()-1;i++) curRes+='9';
        string findRes = res(s);
        if (findRes.empty()) cout<<curRes; else cout<<findRes;
        cout<<endl;
    }
    return 0;
}
