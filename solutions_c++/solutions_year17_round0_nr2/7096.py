#include<iostream>
#include<fstream>
#define ll long long
using namespace std;
int main()
{
    int t,s=0;

    ifstream input;
    input.open("B-large.in");
    ofstream output;
    output.open("codejamas.txt");
    input>>t;
    while (t--)
    {
        s++;
        ll n,x,c=0,i,r,ans=0,zero=0,j;
        input>>n;
        x=n;
        while (x!=0)
        {
            x=x/10;
            c++;
        }
        int a[c]={0};
        x=n;
        for (i=0;i<c;i++)
        {
            r=x%10;
            a[i]=r;
            x=x/10;
        }
        for (i=0;i<c-1;i++)
        {
            if (a[i+1]<=a[i])
            {
            }
            else
            {
                for (j=0;j<=i;j++)
                {
                    a[j]=9;
                    //cout<<a[j];
                }
                a[i+1]--;
            }
        }
       /* for (i=0;i<c-1;i++)
        {
            if (ans==1)
            {
                a[i+1]=9;
            }
            else if (a[i]>a[i+1])
            {
                a[i]--;
                ans=1;
                a[i+1]=9;
            }
        }
        */
        output<<"Case #"<<s<<": ";
        for (i=c-1;i>=0;i--)
        {
            if (a[i]==0&&zero==0)
            {
            }
            else
            {
                zero=1;
                output<<a[i];
            }
        }
        output<<endl;
    }
    return 0;
}
