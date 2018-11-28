#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    int t,i,j,k,l,tt,cnt;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        char s[1000];
        cin>>s>>k;
        l=strlen(s);
        for(i=cnt=0;s[i]!='\0';i++)
            if(s[i]=='-')
            {
                if((i+k)>l)
                {
                    cnt=-1;
                    break;
                }
                for(cnt++,j=i;j<i+k;j++)
                {
                    switch(s[j])
                    {
                    case '+':
                        s[j]='-';
                        break;
                    case '-':
                        s[j]='+';
                        break;
                    }
                }
            }
        if(cnt==-1)
            cout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<tt<<": "<<cnt<<endl;
    }
    return 0;
}
