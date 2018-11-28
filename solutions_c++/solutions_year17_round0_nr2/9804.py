#include<bits/stdc++.h>
using namespace std;
char a[1001];
void minu(int n)
{
    if(n==0){a[0]--;return ;}
    if(a[n]!='0'){a[n]--;return ;}

    a[n]=9+'0';
    minu(n-1);
}

int main()
{
    int t;
    cin>>t;
    for(long h=1;h<=t;h++)
    {

     cout<<"Case #"<<h<<": ";
        cin>>a;

        int l=strlen(a);
        l--;

        while(l>0)
        {
            if(a[l]<a[l-1])
               {

               for(int i=l;i<strlen(a)&&a[i]<'9';i++)
                a[i]='9';

                minu(l-1);
               }
            l--;
        }
        int f=0;
        for(int i=0;i<strlen(a);i++)
           {

            if(a[i]>'0')f=1;
            if(f)cout<<a[i];;
           }
        cout<<endl;
         }
    return 0;
}
