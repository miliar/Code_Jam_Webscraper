#include <bits/stdc++.h>
typedef long long ll;
const int MAX =1e6 +10;
using namespace std;
int arr[22];
int main()
{
    int t ;
    scanf("%d",&t);
    for(int u=1;u<=t;u++)
    {
        ll n;
        scanf("%lld",&n);
        ll num = n;
        //string s = "";
        int k =0;
        while(num)
        {
            int d = num%10;
            arr[k++] = d;
            num/=10;
        }
           // for(int i=0;i<k;i++)
            //cout<<arr[i]<<endl;
        bool fl = 0;
        //cout<<k<<endl;
        while(1)
        {

            for(int i=0;i<k-1;i++)
            {
                fl = 0;
                if(arr[i] < arr[i+1] && !fl)
                {
                    //cout<<i<<endl;
                    fl = 1;
                    arr[i+1]--;
                    //arr[i]--;
                    //break;
                }
                //cout<<fl<<endl;
                if(fl)
                {
                    for(int j=i;j>=0;j--)
                            arr[j] = 9;
                }

            }
            //for(int i=0;i<k;i++)
                //cout<<arr[i]<<endl;
            bool flg = 0;
            for(int i=k-1;i>0;i--)
            {
                if(arr[i] > arr[i-1])
                {
                    flg = 1;
                    break;
                }
            }
            if(!flg)
                break;
        }
        ll ans = 0;
        for(int i=k-1;i>=0;i--)
        {
            ans = (ans*10) + arr[i];
        }
        cout << "Case #" << u << ": " << ans << endl;

    }
    return 0;
}
