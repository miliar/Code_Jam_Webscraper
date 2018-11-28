#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1; i<=t; i++)

    {
        long long n;
         cin>>n;
        string a=to_string(n);
        bool toggle=0; int k; char save;
        for(int j=1; j<a.size(); j++)
        { if(toggle==0)
            {if(a[j]<a[j-1]) {toggle=1; k=j-1; save=a[k]; a[j]='9';}}
          else a[j]='9';
        }

       if(toggle==1)
       { char p;
           for(;k>=0 && a[k]==save; k-- )
         {   p=a[k];
             a[k]='9';

         }
         a[++k]=p-1;
       }

       long long m = stoll(a);
      cout<<"Case #"<<i<<": "<<m<<endl;

    }

    return 0;
}

