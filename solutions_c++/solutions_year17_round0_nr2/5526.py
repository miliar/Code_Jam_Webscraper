#include<iostream>
#include<cstring>
using namespace std;
void rem(char arr[],int pos,int&len)
{
    for(int i=pos;i<len;i++)
        arr[i]=arr[i+1];
    arr[len]='\0';
    len--;
}
int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        char arr[20];
        cin>>arr;
        int len=strlen(arr);
        for(int i=0;i<len;i++){
            if(arr[i]=='0'&&len>1){
                rem(arr,i,len);
                i--;
            }else
                break;
        }
        cout<<"Case #"<<t<<": ";
        int ans=-1;
        for(int i=0;i<len-1;i++)
        {
            if(arr[i]>arr[i+1])
            {
                ans=i;
                break;
            }
        }
        if(ans==-1)
            cout<<arr<<endl;
        else{
            while(ans>=0&&arr[ans-1]==arr[ans])
                ans--;
            if(ans==0){
                if(arr[0]!='1')
                    cout<<(char)(arr[0]-1);
                for(int i=0;i<len-1;i++)
                    cout<<"9";
            }
            else{
                for(int i=0;i<=ans-1;i++)
                    cout<<arr[i];
                cout<<(char)(arr[ans]-1);
                for(int i=ans+1;i<len;i++)
                    cout<<"9";
            }
            cout<<endl;
        }

    }
}
