#include<bits/stdc++.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<cmath>
#include<string>
#include<iomanip>
#include<map>
using namespace std;
typedef long long int ll;
#define boost ios_base::sync_with_stdio(false); cin.tie(NULL);


string s;
ll t, id;
bool b;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outputfilenew1.out","w",stdout);


    cin>>t;   ll count=1;
    while(count<=t)
    {

        cin>>s;
        ll sz=s.size();
        b=id=0;
        for(int i=1; i<sz; i++)
            if(s[i]<s[i-1])
            { b=1; id=i-1; break;}

        while(s[id]==s[id-1]&&id>=0)   id--;
        cout<<"Case #"<<count<<": ";
        if(!b) cout<<s;
        else
        {
                     s[id]--;
                     for(int i=id+1; i<sz; i++)  s[i]=9+'0';
                     if((s[0]-'0')!=0) cout<<s[0];
                     for(int i=1; i<sz; i++)   cout<<s[i];
        }
        count+=1;
        cout<<endl;
    }
    return 0;
}
