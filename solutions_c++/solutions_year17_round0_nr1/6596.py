#include <iostream>
using namespace std;

int main() {
    int k;
    int T;
    cin>>T;
    int t = 1;
    while(T--)
    {
        char s[100000]={0};
        cin>>s;
        cin>>k;
        //cout<<s<<" "<<k<<endl;
        int start = 0;
        int cnt=0;
        while(s[start+k-1]!=0)
        {
            int i=start;
            for(i=start;s[i]!=0;i++)
            {
                if(s[i]=='-')
                {
                    cnt++;
                    break;
                }
            }
            start=i;
            if(s[i]!=0 && s[i+k-1]!=0)
            {
                //Flip
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                }
            }
            //cout<<s<<endl;
        }
        int flag=0;
        for(int i=0;s[i]!=0;i++)
        {
            if(s[i]=='-')
            {
                flag=1;
            }
        }
        if(flag==0)
        {
            cout<<"Case #"<<t<<": "<<cnt<<endl;
        }
        else
        {
            cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        }
        t++;
    }
    return 0;
}
