#include <bits/stdc++.h>
using namespace std;
string n;
long long int size,i,j,k=0,l=0,m;
void check()
{      int t=0;
        size=n.length();
        for(i=0;i<size-1;i++)
        {   
            if((n[i]-48)>(n[i+1]-48))
            {   
                if(n[i]=='0'||n[i]=='1')
                {   n[k]='#';
                    k++;
                    for(j=1;j<size;j++)
                    n[j]='9';
                }
                else
                {      n[i]=(n[i]-1);
                    for(j=i;j<size;j++)
                          n[j+1]='9';
                           t=1;
                        //cout<<n[i]<<endl;
                        
                }
                
            }
        }
        if(t==1)
        {
            check();
        }
        else
        return;
}

int main()
{
    int t;
   // string n;
   // long long int size,i,j,k=0,l=0,m;
    cin>>t;
    while(t--)
    {   l++;
           k=0;
        cin>>n;
        size=n.length();
        check();
        cout<<"Case #"<<l<<": ";
       // cout<<"n"<<n<<endl;
        for(i=0;i<size;i++)
        {
            if(n[i]!='#')
            cout<<n[i];
        }
        cout<<endl;
        
        
    }
    //cout << "Hello World!" << endl;
    return 0;
}
