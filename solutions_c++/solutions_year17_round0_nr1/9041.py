#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,n,k,j,cs=0,cnt;
    FILE *fp;
    fp = fopen("A_small.txt","w");
    bool flag;
    string s;
    cin>>t;
    while(t--)
    {

        flag=true;
        cnt=0;
        cin>>s;
        n=s.size();
        cin>>k;
        for(i=0; i<n;i++)
        {
            if(s[i]=='-')
            {
                for(j=0; j<k; j++)
                {
                    if(i+j<n)
                    {
                        if(s[i+j]=='-')
                            s[i+j]='+';
                        else
                            s[i+j]='-';
                    }
                    else
                    {
                        flag=false;
                        break;
                    }
                }
                cnt++;
            }

        }
        if(flag)
            fprintf(fp,"Case #%d: %d\n",++cs,cnt);
        else
            fprintf(fp,"Case #%d: IMPOSSIBLE\n",++cs,cnt);

    }
    return 0;
}
