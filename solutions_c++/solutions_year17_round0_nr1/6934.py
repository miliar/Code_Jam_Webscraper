#include<iostream>
#include<stdio.h>
#include<string.h>
#include<limits.h>
using namespace std;
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int t;
    cin>>t;
    int tno=0;
    while(t-->0)
    {
        tno++;
        char s[1001];
        int k;
        cin>>s>>k;
        int n=strlen(s);
        int flip=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')
            {

                for(int j=i;j<(k+i)&&j<n;j++)
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';

                if(k+i<=n)
                flip++;
                else
                    flip=INT_MIN;

            }
        }

        if(flip<0)
            cout<<"Case #"<<tno<<": IMPOSSIBLE"<<endl;
            else
            cout<<"Case #"<<tno<<": "<<flip<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
