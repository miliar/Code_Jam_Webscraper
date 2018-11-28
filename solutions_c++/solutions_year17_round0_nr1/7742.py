#include <iostream>
using namespace std;

int main() {
        ios_base::sync_with_stdio(false); cin.tie(0);
       freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
        int t,y;cin>>t;
        for(int z=1;z<=t;z++)
        {string s;y=0;
        cin>>s;int k;cin>>k;
        int l=s.length();int arr[l];
        for(int i=0;i<l;i++)
        if(s[i]=='-')arr[i]=1;
        else arr[i]=0;
        for(int i=0;i<=l-k;i++)
        {
            if(arr[i]%2==0)continue;
            else
            {for(int j=i;j<=i+k-1;j++)
            arr[j]++;
            y++;}
        }
        int i;
        for(i=l-k+1;i<l;i++)
        if(arr[i]%2==1)break;
        if(i==l)
        printf("Case #%d: %d\n", z, y);
        else
        printf("Case #%d: IMPOSSIBLE\n",z);
        }
        
}
