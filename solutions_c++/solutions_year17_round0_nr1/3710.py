#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int t,i,k,j,l;
    char s[1005];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        cin>>k;
      //  cout<<" s = "<<s<<endl;
      //  cout<<" k = "<<k<<endl;
        int len = strlen(s);
        int count = 0;
        for(j=0;j<len-k;j++){
            if(s[j]=='-')
            {
                for(l=0;l<k;l++)
                {
                    s[j+l]=='-'?s[j+l]='+':s[j+l]='-';
                }
                count++;
            }

        }
        int x=0;
        for(l=j;s[l];l++){
            if(s[l]!='-') break;
        }
        if(l==len) {count++; cout<<"Case #"<<i<<": "<<count<<endl;}
        else{
            for(l=j;s[l];l++){
                if(s[l]!='+') break;
            }
            if(l==len) {cout<<"Case #"<<i<<": "<<count<<endl;}
            else {cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;}
        }
    }
    return 0;
}
