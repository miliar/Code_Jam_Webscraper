#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        char arr[1002];
        int k;
        cin>>arr>>k;
        int ans=0;
        int len=strlen(arr);
        for(int i=0;i<len;i++){
            if(arr[i]=='-'){
                if(i+k-1>=len)
                {
                    ans=-1;
                    cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
                    break;
                }

                ans++;
                for(int j=1;j<k;j++)
                    arr[i+j]=arr[i+j]=='+'?'-':'+';
            }
        }
        if(ans!=-1)
            cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
