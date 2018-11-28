#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    long long t,n,cs=0,i;
    FILE *fp;
    fp = fopen("B_small.txt","w");
    cin>>t;
    while(t--)
    {
        cin>>s;
        n=s.size();

        for(i=0; i<n-1; i++)
        {
            if(s[i]>s[i+1])
            {
                if(s[i+1]=='0' && s[i]=='1')
                {
                    for(i=0; i<n-1; i++)
                        s[i]='9';
                    s[i]='\0';
                    break;
                }
                else
                {
                    bool flag=false;
                    s[i]--;
                    int k=i;
                    while(i>0 && s[i]<=s[i-1])
                    {
                        s[i]='9';
                        i--;
                        flag=true;
                    }
                    if(flag)
                        s[i]--;

                    for(k++; k<n; k++)
                        s[k]='9';
                }
            }
        }


        ///cout<<s<<endl;
        fprintf(fp,"Case #%lld: %s\n",++cs,s.c_str());
        s.clear();

    }
    return 0;
}

