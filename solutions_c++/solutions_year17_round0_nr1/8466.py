#include<iostream>
#include<string.h>
using namespace std;
int check(char[]);
int main()
{
    int t;
    cin>>t;
    for (int p = 1; p <= t; ++p)
    {
        int k,i,j,countd=0,l;
    char s[10000];
    cin>>s;
    cin>>j;
    l=strlen(s);
    for(k=0;k<l;k++)
    {
        if(s[k]=='-')
        {

            {
                for(i=k;i<k+j;i++)
                {
                    if(s[i]=='-')
                        s[i]='+';
                    else
                        s[i]='-';
                }
            countd++;
            }
        }

    }
    if(check(s)==0)
        cout << "Case #" << p << ": " << "IMPOSSIBLE" << endl;
    if(check(s)==1)
        cout << "Case #" << p << ": " << countd << endl;

    }

}
int check(char s[])
{
    int i;
    for(i=0;i<strlen(s);i++)
    {
        if(s[i]=='-')
            return 0;
    }
    return 1;
}
