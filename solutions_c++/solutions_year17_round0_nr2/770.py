#include <iostream>

using namespace std;

bool check(int *a, int l)
{
    int i;
    for(i=0;i<l-1;i++)
        if(a[i]<a[i+1]) return false;
    return true;
}

void clearup(int *a, int &l)
{
    int i;
    for(i=0;i<l;i++)
    {
        if(a[i]>=0) continue;
        a[i]+=10;
        a[i+1]-=1;
    }
    if(a[l-1]==0)
    {
        l--;
        for(i=0;i<l;i++) a[i]=9;
    }
}

void mymain(int t)
{
    long long n;
    int a[20];
    int i,l,j;
    cin>>n;
    cout<<"Case #"<<t<<": ";
    if(n<10)
    {
        cout<<n<<endl;
        return;
    }
    l=0;
    while(n>0)
    {
        a[l]=n%10;
        n=n/10;
        l++;
    }
    while(!check(a,l))
    {
        for(i=0;i<l-1;i++)
        {
            if(a[i]>=a[i+1]) continue;
            a[i]=9;
            a[i+1]--;
            //clearup(a,l);
            for(j=0;j<i;j++) a[j]=9;
            if(a[l-1]==0) l--;
        }
    }
    for(i=l-1;i>=0;i--)
    {
        n*=10;
        n+=a[i];
    }
    cout<<n<<endl;
}

int main()
{
    int T,t;
    cin>>T;
    for(t=0;t<T;t++) mymain(t+1);
    return 0;
}
