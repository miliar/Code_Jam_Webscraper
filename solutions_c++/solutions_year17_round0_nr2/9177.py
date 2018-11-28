
//codejam
#include <bits/stdc++.h>
using namespace std;
#define ll long long unsigned

string getAns(string n)
{
    vector<char>ans;
    char c=n[0];
    while(1)
    {   char c=n[0];
        if(c > n[1])
        break;
        else
        {
            ans.push_back(n[0]);
            n.erase(0,1);
        }
    }
    //cout<<n<<"--";
    if(n.size() == 1)
    {
    ans.push_back(n[0]);
    n.erase(0,1);
    }
    if(n.size() > 1)
    {
        if(n[0] != '1')
        {
            ans.push_back(n[0] - 1);
            for(int i=1;i<n.size();i++)
            ans.push_back('9');
        }
        else
        {
            char tmp=ans.back();
            tmp--;
            ans.pop_back();
            ans.push_back(tmp);
            for(int i=0;i<n.size();i++)
            ans.push_back('9');
        }
    }
    bool f=0;
        while(find(ans.begin(), ans.end(), '0') != ans.end() )
        {
            
            ans.erase(ans.begin(), ans.begin() + 1);
           if(f)
            ans.push_back('9');
            f=1;
        }
        string aa="";
    for(int i=0;i<ans.size();i++)
    aa+=ans[i];
    //printf("\n");
    return aa;
}

int main()
{
    ll t;
    scanf("%llu",&t);
    for(ll i=1;i<=t;i++)
    {   //another for large input :)
        string n;
        cin >> n;
       printf("Case #%llu: ",i);
       if(n.size() == 1)
       cout<<n<<endl;
       else if(n[0]=='1' && n[1]=='0')
       {
           for(int i=1;i<n.size();i++)
           cout<<'9';
           cout<<endl;
       }
       else
       {   string curr=n;
           while(1)
            {
           string prev=curr;
            curr=getAns(prev);
            if(curr == prev)
            {
        cout<<curr<<endl;break;}
            }
       }
    }
    return 0;
}
