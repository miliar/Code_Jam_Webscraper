#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define file_input freopen("in.txt","r",stdin)
#define file_output freopen("op.txt","w",stdout)
int tidy_check(int n)
{
    int prev_digit=n%10;
    n=n/10;
    while(n!=0)
    {
        int next_digit=n%10;
        n=n/10;
        if(next_digit>prev_digit)
            return 0;
        prev_digit=next_digit;
    }
    return 1;
}
int main() {
    file_input;
    file_output;
    /*ll dp[70]={0};
    dp[0]=1;
    dp[1]=2;
    for(int i=1;i<65;i++)
        dp[i]=dp[i-1]+pow(2,i);

    /*for(int i=0;i<30;i++)
        cout<<i<<' '<<dp[i]<<endl;
    int test_case;
    cin>>test_case;
    for(int t=1;t<=test_case;t++){
        ll ans=0;
        ll n,k;
        cin>>n>>k;
        int pos=0;
        while(true)
        {
            if(dp[pos]>=k)
                break;
            pos++;
        }
        ll m=n;
        while(pos>0)
        {
            m=m/2;
            pos--;
        }
        ll mx=m/2;
        ll mn=mx;
        if(m%2==0)
            mn--;
        cout<<n<<' '<<k<<endl;
        cout<<"Case #"<<t<<": "<<mx<<' '<<mn<<endl;
    }*/
    int test_case;
    cin>>test_case;
    for(int t=1;t<=test_case;t++)
    {
        int n,k;
        cin>>n>>k;
        int ar[1005]={0};
        int l=0;
        ar[n+1]=1;
        ar[0]=1;
        int mx=0;
        for(int i=0;i<k;i++)
        {
            mx=0;
            int c=0;
            for(int j=1;j<=n+1;j++)
            {
                if(ar[j]==0)
                {
                    c++;
                    continue;
                }
                if(c>mx)
                {
                    mx=c;
                    l=j;
                }
                c=0;
            }
           // cout<<l<<' '<<r<<endl;
            int mid=mx/2;
            if((mx)%2!=0)
                mid++;
            ar[l-mid]=1;
        }
        int xx=mx/2;
        int yy=xx;
        if(mx%2==0)
            yy--;
        cout<<"Case #"<<t<<": "<<xx<<' '<<yy<<endl;
    }
	return 0;
}
