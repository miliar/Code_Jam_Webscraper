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
        string s;
    int k;
    cin>>s;
    scanf("%d" , &k);
    string q = s;
    int sum1 =0 , sum2 = 0;
    for(int i = 0 ; i+k-1 < s.size() ; ++i)
    {
        if(q[i]=='-')
        {
            sum1++;
            for(int j = 0 ; j<k ; ++j)
                if(q[i+j]=='-') q[i+j]='+';
                else q[i+j]='-';

        }
    }
    for(int i = 0 ; i+k-1 < s.size() ; ++i)
    {
        if(s[i]=='-')
        {
            sum2++;
            for(int j = 0 ; j<k ; ++j)
                if(s[i+j]=='-') s[i+j]='+';
                else s[i+j]='-';

        }
    }
    int ans = -1;
    int x = q.find("-");
    int y = s.find("-");
    if(x!=-1 && y!=-1) printf("Case #%d: IMPOSSIBLE\n" , n++);
    else if(x==-1 && y==-1) printf("Case #%d: %d\n" , n++ , min(sum1 , sum2));
    else if(x==-1) printf("Case #%d: %d\n" , n++ , sum1);
    else printf("Case #%d: %d\n" , n++ , sum2);
    }
    return 0;
}
