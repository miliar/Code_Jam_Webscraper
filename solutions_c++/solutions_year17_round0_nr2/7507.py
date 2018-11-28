#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<stack>
#include<map>
#define int long long
using namespace std;
const int MX=2e5+10;
string ans="";
vector<int>p[MX];
map<pair<int,int>,int>mp;
bool used[MX];
int a[MX];
int n,m,k,stx,sty,is_ans=1;
string convert_tostring(int num)
{
    string ans="";
    while(num)
    {
        ans+=char(num%10+48);
        num/=10;
    }
    reverse(ans.begin() , ans.end());
    return ans;
}
bool is(int num)
{
    int mn=num%10;
    while(num)
    {
        if(num%10>mn) return 0;
        mn=min(mn,num%10);
        num/=10;
    }
    return 1;
}
string my_tester(int num)
{
    while(!is(num))
    {
        num--;
    }
    return convert_tostring(num);
}
string my_solve(string s)
{
    string ans="";
    int mx=s[0]-48,last;
    last=mx;
    ans=char(mx+48);
    for(int i=1;i<s.size();i++)
    {
        int now=s[i]-48;
        if(now<mx)
        {
            ans[ans.size()-1]=char(last-1+48);
            while(i++<s.size())
            {
                ans+="9";
            }
            break;
        }
        last=now;
        mx=max(mx,now);
        ans+=char(now+48);
    }
    if(ans[0]=='0')
    {
        ans="";
        for(int i=0;i<s.size()-1;i++) ans+="9";
    }
    s=ans;
    mx=s[0]-48;
    for(int i=0;i<s.size();i++)
    {
        int now=s[i]-48;
        if(now<mx)
        {
            return my_solve(s);
        }
        mx=max(mx,now);
    }
    return ans;
}
main()
{
//    ifstream cin("B-large.in");
//    ofstream cout("B-large.out");
    int test;
    cin>>test;
    string n;
    for(int i=1;i<=test;i++)
    {
        cin>>n;
        cout<<"Case #"<<i<<": "<<my_solve(n)<<endl;
    }
    return 0;
//    cin>>n;
    for(int i=1;i<=1e7;i++)
    {
        string q1=my_solve(convert_tostring(i));
        string q2=my_tester(i);
        if(q1!=q2)
        {
            cout<<i<<endl;
            cout<<q1<<" "<<q2<<endl;
            return 0;
        }
        if(i%100000==0) cout<<i<<endl;
    }
    cout<<"ACCEPT";
    return 0;
    for(int i=1;i<=1000;i++)
    {
        if(is(i))
        {
            cout<<i<<endl;;
        }
    }
}

/*
3127
2999

1099
0099

1180
1179
4
132
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

*/
