#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    int n = 1;
    cin>>t;
    while(t--)
    {
    string s,q;
    cin>>s;
    q = string(s.size() , '1');
    for(int i = 0 ; i<q.size() ; i++)
        {
          for(int j =  i ; j<s.size() ; j++) q[j] = s[i];
            if(q>s)
            {
                q[i] = s[i]-1;
                for(int j =  i+1 ; j<s.size() ; j++) q[j]='9';
                break;
            }
        }
        stringstream m;
        long long x;
        m<<q;
        m>>x;
        printf("Case #%d: %lld\n" , n++ , x);
    }
    return 0;
}
