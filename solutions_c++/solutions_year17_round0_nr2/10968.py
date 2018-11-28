#include<bits/stdc++.h>
using namespace std;
#define max 1001
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int n,t,i,l,r=0,f=0,m=0,o=0,j,x=0;
    cin>>t;
    for(j=1;j<=t;j++)
    {

        cin>>n;
        o=n;
        l=(n==0)?1:(int)log10(n)+1;
        int a[max]{0};
        f=0;
        if(n<10)
        {
                cout<<"Case #"<<j<<": "<<n<<endl;
                continue;
        }
        else
        {
            x=0;
            while(f==0)
            {
                if(n<10)
                {
                    cout<<"Case #"<<j<<": "<<o<<endl;
                    x=1;
                    break;
                }
                else
                {
                    for(i=0;i<l;i++)
                    {
                        r=n%10;
                        n=n/10;
                        a[i]=r;
                    }
                    for(i=0;i<(l-1);i++)
                    {
                        if(a[i]>=a[i+1])
                        {
                            f=1;
                            m=o;
                            continue;
                        }
                        else
                        {
                            f=0;
                            m=o;
                            break;
                        }
                    }
                }
            o=o-1;
            n=o;
            l=(n==0)?1:(int)log10(n)+1;
            }
            if(x==0){
            cout<<"Case #"<<j<<": "<<m<<endl;}
            else{continue;}
        }


    }
return 0;
}
