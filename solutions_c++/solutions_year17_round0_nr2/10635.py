#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("output.txt","w+",stdout);

    ios::sync_with_stdio(false);

    int t,n,counter=0;

    cin>>t;

    while(t--)
    {
        string n;

        cin>>n;

        char maxx=n[0];

        for(int i=1;i<n.length();i++)
        {
            if(n[i]>maxx)
            {
                maxx= n[i];
            }

            if(n[i]<maxx)
            {
                int start=i-1;

                for(int j=i-1;j>0;j--)
                {
                    if(n[j]==n[j-1])
                    {
                        start=j-1;
                    }
                }

                n[start]--;

                for(int j=start+1;j<n.length();j++)
                {
                    n[j]='9';
                }
            }
        }

        //ong long x = atol(n.c_str());

        //printf("Case #%d: %s\n",++counter,n.c_str());
        printf("Case #%d: ",++counter);

        bool flag = false;

        for(int i=0;i<n.length();i++)
        {
            if(n[i]!='0')
                flag = true;

            if(flag)
                putchar(n[i]);
        }

        printf("\n");
    }

    return 0;
}
