#include<iostream>
#include<string>
using namespace std;
int main(){
int t;
cin>>t;int co=1;
while(t>=co)
{
    string st;
    cin>>st;
    int len=st.length(),k;
    int mat[len];int count=0,flg=0;
    for(int i=0;i<len;i++)
    {
        if(st[i]=='+')
            mat[i]=1;
        else
            mat[i]=-1;
    }
    cin>>k;
    for(int i=0;i<len;i++)
    {
        if(mat[i]==-1)
        {
            if(i+k>len)
               {
                flg=1;
                break;
               }
            else{
                for(int q=0;q<k;q++)
            {
                mat[i+q]=mat[i+q]*-1;
            }
        count++;
        }
        }

    }
    cout<<"Case #"<<co<<": ";
    if(flg!=1)
        cout<<count<<endl;
    else
        cout<<"IMPOSSIBLE"<<endl;

co++;}



}
