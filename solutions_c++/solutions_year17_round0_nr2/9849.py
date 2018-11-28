#include<bits/stdc++.h>
#define f first
#define s second

using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    //freopen("in.cpp","r",stdin);
    freopen("A7.txt","r",stdin);
    freopen("out8.txt","w",stdout);
    long long t,n,k,q,l,r,i,j,x,y,z,x1,x2,y1,y2;
    cin>>t;l=1;
    while(t--)
    {
        cin>>n;x=n;
        vector<long long>a,b;
        while(x!=0)
        {
           y=x%10;a.push_back(y);
           x=x/10;
        }
        y=a.size();
        if(y==1)
            cout<<"Case #"<<l<<": "<<n<<endl;
        else
        {
           for(i=0;i<y-2;i++)
            {
            if(a[i]==0&&a[i+1]==0)
            {
                a[i]=9;
            }
            else if(a[i]<a[i+1]&&i==0)
            {
                a[i]=9;a[i+1]--;
            }
            else if(a[i]<a[i+1])
            {
                a[i]=a[i-1];a[i+1]--;
            }
            }
            if(a[y-2]<a[y-1])
            {
                a[y-1]--;
                for(i=0;i<y-1;i++)
                    a[i]=9;
            }
            if(a[y-1]==0)
                {a.erase(a.begin()+y-1);y--;}
            reverse(a.begin(),a.end());
            cout<<"Case #"<<l<<": ";
            for(i=0;i<y;i++)
                cout<<a[i];
            cout<<endl;
        }
      l++;
    }
    return 0;
}


