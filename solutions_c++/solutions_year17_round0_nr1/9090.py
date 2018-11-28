#include<bits/stdc++.h>
using namespace std;
string s;
int start;
int  test;
int k;
int main()
{
    //freopen("test.inp","r",stdin);
    //freopen("test.out","w",stdout);
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        cin>>s>>k;
        printf("Case #%d: ",t);
        int cnt=0;
        int check=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-'&&s.size()-i<k)
            {
                printf("IMPOSSIBLE\n");
                check=1;
                break;
            }
            if(s[i]=='-')
            {
                cnt++;
                for(int j=0;j<k;j++)
                {
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
                //cout<<s<<"\n";
            }
        }
        if(check==0)
        printf("%d\n",cnt);
    }
}

