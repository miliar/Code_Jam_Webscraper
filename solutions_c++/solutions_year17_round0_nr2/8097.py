#include<bits/stdc++.h>
using namespace std;
int main()
{//freopen("B-large.in","r",stdin);
//freopen("b2.txt","w",stdout);
    int n;

cin>>n;
for(int xx=1;xx<=n;xx++)
{
    string a;
    cin>>a;
   // cout<<a;
    for(int i=0;i<a.length()-1;i++)
    {
        if(a[i]>a[i+1])
        {int j=i;
            while(j+1)
            {if(a[j]-a[j-1]>0)
                {a[j]=char(a[j]-1);//cout<<" dsD "<<a[j];
                break;}
            else
            {if(j==0)
                {
                    a[j]='a';
                    break;
                }
                a[j]='9';
                j--;

            }
            }
            i++;
            while(i<a.length())
            {
                a[i]='9';
                i++;
            }
        }
    }
     if(a[0]=='a')
     {
     cout<<"Case #"<<xx<<": ";

        for(int i=1;i<a.length();i++)
        cout<<a[i];
        cout<<endl;
     }
     else if(a[0]=='0'&&a[1]!='0')
     {cout<<"Case #"<<xx<<": ";

        for(int i=1;i<a.length();i++)
        cout<<a[i];
        cout<<endl;

     }

     else
     cout<<"Case #"<<xx<<": "<<a<<endl;
}
}
