#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int arr[1002];
int temp[1002];
int main()
{
    freopen("in.txt.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int tt=0;
    while(t--){
        string a;
        int k;
        cin>>a;
        cin>>k;
        cout<<"Case #"<<++tt<<": ";
        int len = a.length();
        for(int i=0;i<len;i++){
            if(a[i]=='+')
                arr[i]=0;
            else
                arr[i]=1;
            temp[i]=0;
        }

        int cnt = 0,curr=0;
        for(int i=0;i<len-k+1;i++){
            curr = temp[i]+curr;
            if((arr[i]+curr)%2==0)
                continue;
            temp[i+k]=-1;
            curr++;
            cnt++;
        }
        int flg=0;
        for(int i=len-k+1;i<len;i++){
                curr += temp[i];
            if((arr[i]+curr)%2!=0)
            {
                flg=1;
                break;
            }
        }
        if(flg)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<cnt<<endl;
    }
}
