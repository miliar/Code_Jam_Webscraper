#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("hellolarge.txt", "w", stdout);
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        string s;cin>>s;
        int len=s.size();
        vector<int> arr(len);
        for(int i=0;i<len;i++)
            arr[i]=s[i]-'0';
            int k=len;
        for(int i=1;i<len;i++)
        {
            if(arr[i]<arr[i-1])
            {
                k=i-1;
                for(int zz=0;zz<k;zz++)
                {
                    if(arr[zz]==arr[k])
                    {
                        k=zz;break;
                    }
                }
                break;
            }
        }
        //cout<<k<<endl;
        if(k<len)
        {
            arr[k]--;
            for(int i=k+1;i<len;i++)
                arr[i]=9;
        }
        cout<<"Case #"<<t<<":"<<" ";
        for(int i=0;i<len-1;i++)
        {
            if(arr[i]!=0)
            cout<<arr[i];
        }
        cout<<arr[len-1]<<endl;
}
}
