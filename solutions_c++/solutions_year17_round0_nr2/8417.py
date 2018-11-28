#include <bits/stdc++.h>
#define ll long long
using namespace std;
int arr[20];
void solve(int l)
{
    for(int i=0;i<l-1;i++)
    {
        if(arr[i]>arr[i+1])
        {
            arr[i]--;
            for(int j=i+1;j<l;j++)
            {
                arr[j]=9;
            }
            break;
        }

    }
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out2.txt","w",stdout);
    int test,t=1;

    scanf("%d",&test);

    while(test--)
    {
        string n;
        cin>>n;
        int l=n.size();
        //int digit[l];
        for(int i=0;i<l;i++)
        {
            arr[i]=n[i]-'0';
        }
        printf("Case #%d: ",t++);
        //cout<<n<<endl;
        for(int i=1;i<=l;i++)
        {
            solve(l);
        }
        for(int i=0;i<l;i++)
        {
            if(arr[i]>0)
                cout<<arr[i];
        }
        cout<<endl;

    }
    return 0;
}
