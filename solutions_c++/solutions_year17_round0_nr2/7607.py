#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    while(x<=t)
    {
         long long int n,k;
         cin>>n;
         k=n;
         vector<char>s;
         int i=0;
         for(i=0;k>0;i++)
         {
             int x=k%10;
             char c=x+'0';
             s.push_back(c);
             k/=10;
         }
        // cout<<s<<endl;
         int l=s.size();
         vector<char> arr(l);
         for(i=0;i<l;i++)
         {
             arr[i]=s[l-i-1];
         }

         for(i=0;i<l;i++)
         {
             for(int j=1;j<l;j++)
             {
                 if(arr[j-1]>arr[j])
                 {
                     arr[j-1]--;
                     for(j;j<l;j++)
                          arr[j]='9';
                 }
             }
         }
         cout<<"Case #"<<x<<": ";
          i=0;
          //cout<<arr<<endl;
         while(arr[i]=='0')
             i++;
         for(i;i<l;i++)
            cout<<arr[i];
         cout<<endl;
      x++;
    }
    return 0;
}
