#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("pancakes2.in", "r", stdin);
freopen("pancakes2.out", "w", stdout);
int t,k,i,l,count,j,n,flag=0;
string s;
cin>>t;
for(i=1;i<=t;i++)
{
    count=0;
    flag=0;
    cin>>s>>k;
    n=s.size();
    for(j=0;j<n;j++)
    {
        l=k-1;
        if(j+l>n || (j+l)==n){
        while(n--){
                if (s[n]=='-')
                {
                    flag=1;
                    break;
                }
        }
        }
        else{
            if (s[j]=='-'){
                count++;
                while (l>=0) {
                    if(s[j+l]=='+')
                        s[j+l]='-';
                    else
                        s[j+l]='+';
                    l--;
                }
            }
        }

    }
    if(flag==0)
            cout<<"Case #"<<i<<": "<<count<<endl;
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
}
return 0;
}
