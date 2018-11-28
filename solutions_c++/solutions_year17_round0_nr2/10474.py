#include<bits/stdc++.h>
using namespace std;
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t,c=0;
    cin>>t;
    if(1<= t <=100)
        {
            while(t--)
            {
                c++;
                int i=1,k,m;
                string n;
                cin>>n;
                int b=atoi(n.c_str());
                if(1<=b<=1000 )
                {
                    k=n.length();
                    while(n[i]!=NULL)
                    {
                        if(n[i-1]>n[i])
                        {
                            n[i-1]=n[i-1]-1;
                            if(n[i-2]>n[i-1])
                            {
                                n[i-2]=n[i-2]-1;
                                i--;
                            }
                            break;
                        }
                        i++;
                    }
                    for(m=i;m<=k;m++)
                    {
                        n[m]='9';
                    }
                    if(n[0]=='0')
                    {
                        cout<<"Case #"<<c<<": "<<n.substr(1,k)<<endl;
                    }
                    else
                    {
                        cout<<"Case #"<<c<<": "<<n<<endl;
                    }
                }
            }
    }
    return 0;
}
