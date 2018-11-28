#include<bits/stdc++.h>
using namespace std;
bool check(long long int n)
{
    char str[50];
    sprintf(str, "%lld", n);
    //cout<<str<<endl;
    for(int i=1; i<strlen(str); i++)
    {
        if(str[i]<str[i-1]) return false;
    }
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int i=1; i<=test; i++)
    {
        long long int n;
        scanf("%lld",&n);
        if(check(n))
        {
            cout<<"Case #"<<i<<": "<<n<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": ";
            char str[50];
            sprintf(str, "%lld", n);
            // cout<<str<<endl;
            char s[50];
            int j;
            for( j=0; j<strlen(str); j++)
            {
                s[j]='1';
            }
            s[j]='\0';

            long long p;

            char* pEnd;
            p = strtoll (s, &pEnd, 10);
            // cout<<p<<endl;
            if(n<p)
            {
                for( j=0; j<strlen(str)-1; j++)
                {
                    cout<<9;
                }
                cout<<endl;
            }
            else
            {
                long long ans=n;
                ans=n-1;
             long long    int i=1;
            long long     int k=1;
                while(!check(ans))
                {
                    i=i*10;
                    long long rem=ans%i;
                    ans=ans-rem;
                    char str[50];
                    sprintf(str, "%lld", ans);
                    for(int j=strlen(str)-1; j>=(strlen(str)-k); j--)
                    {
                        str[j]='9';
                    }
                    char* pEnd;
                    ans = strtoll (str, &pEnd, 10);
                    ans=ans-i;
                    k++;

                }
                cout<<ans<<endl;


            }

        }

    }
}
