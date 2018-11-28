#include <iostream>
using namespace std;
int frontSide(string str,int r)
{
    int count=0;
    for(int i=0;i<str.length();i++)
    {
        if(str[i]=='-'&&i<str.length()-r+1)
        {
            int k=i;count++;
            //cout<<" "<<str<<endl;
            for(;k<i+r;k++){
                if(str[k]=='+')str[k]='-';
                else
                str[k]='+';
            }
            //i=k;
        }
    }//cout<<str;
    int flag=1;
    for(int i=0;i<str.length();i++)if(str[i]!='+'){flag=0;break;}
    if(flag==1)return count;
    else
    return -1;
}
int backSide(string str,int b)
{
    int count=0;
    for(int i=str.length();i>=b-1;i--)
    {
        if(str[i]=='-')
        {
        count++;
        for(int k=i;k>i-b;k--){
        if(str[k]=='+')str[k]='-';
                else
                str[k]='+';
        }
        }
    }
    int flag=1;
    for(int i=0;i<str.length();i++)if(str[i]!='+'){flag=0;break;}
    if(flag==1)return count;
    else
    return -1;
}
int main() {

    int t;
    cin>>t;
    int s=0;
    while(s<t)
    {
        string str;
        int test;
        cin>>str;
        int k;
        cin>>k;
        int b,f;
        b=backSide(str,k);
        f=frontSide(str,k);
        if(b==-1)
        {
            if(f==-1)test=-1;
            else
            test=f;
        }
        else
        {
            if(f==-1)test=-1;
            else
            test=b>f?b:f;
        }
        cout<<"Case #"<<s+1<<": ";
        if(test!=-1)cout<<test<<endl;
        else
        cout<<"IMPOSSIBLE\n";
        s++;
    }
	return 0;
}
