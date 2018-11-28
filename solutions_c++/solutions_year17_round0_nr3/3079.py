#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long t,k,n,br1,br11,br2,br21,br,x,n1,n2;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n>>k;
        long long g=0;
        br=1;
        br1=0;
        br2=0;
        br11=0;
        br21=0;
        x=0;
        if(n%2==0)
        {
            br1=1;
            br2=1;
            k--;
            n1=n/2;
            n2=n/2-1;
            g=1;
        }
        ///k--;
        if(!k)
        {
            x=1;
                cout<<"case #"<<i+1<<": ";
                if(n==1)
                    cout<<"0 0"<<endl;
                    else
                if(n%2==0)
                    cout<<n/2<<" "<<n/2-1<<endl;
                else
                    cout<<n/2<<" "<<n/2<<endl;

        }
        if(!g)
        while(1!=2&&!x)
        {
            if(k>br)
            k-=br;
            else
            {
                x=1;
                ///cout<<br1<<" "<<br2<<endl;
                cout<<"case #"<<i+1<<": ";
                if(n==1)
                    cout<<"0 0"<<endl;
                else if(n%2==0)
                    cout<<n/2<<" "<<n/2-1<<endl;
                else
                    cout<<n/2<<" "<<n/2<<endl;
            }
            if(n%2==0)
            {
                br1=br;
                n1=n/2;
                n2=n/2-1;
                br2=br;
                break;
            }
             br=br*2,n/=2;
        }

        ///cout<<n<<" "<<k<<" "<<br1<<" "<<br2<<" "<<n1<<" "<<n2<<endl;
        while(k>=0&&!x)
        {
            ///cout<<n1<<" "<<br1<<" "<<n2<<" "<<br2<<endl;
            ///system("pause");
            if(k>br1)
            {
                k=k-br1;
            }
            else
            {
                x=1;
                ///cout<<n1<<endl;
                cout<<"case #"<<i+1<<": ";
                if(n1==1)
                    cout<<"0 0"<<endl;
                else if(n1%2==0)
                    cout<<n1/2<<" "<<n1/2-1<<endl;
                else
                    cout<<n1/2<<" "<<n1/2<<endl;
                break;
            }
            if(k>br2)
            {
                k=k-br2;
            }
            else
            {
                x=1;
                ///cout<<n2<<endl;
                cout<<"case #"<<i+1<<": ";
                if(n2==1)
                    cout<<"0 0"<<endl;
                else if(n2%2==0)
                    cout<<n2/2<<" "<<n2/2-1<<endl;
                else
                    cout<<n2/2<<" "<<n2/2<<endl;
                    break;

            }

            if(n1%2==0)
            {
                br11+=br1;
                br21+=br1;
                n2=n1/2-1;
                n1=n1/2;
                br21+=2*br2;
            }
            else
            {
                br11+=br1*2;
                n1=n1/2;
                n2=n2/2-1;
                br21+=br2;
                br11+=br2;
            }
            br1=br11;
            br2=br21;
            br11=0;
            br21=0;
        }
    }
}
