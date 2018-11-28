#include<iostream>
using namespace std;
int pancakes()
{
    string st;int c=0;
    cin>>st;int k;
    cin>>k;
    for(int l=0;l<st.length();l++)
    {

        if(st[l]=='-')
        {
            c++;
            if((l+k)>st.length())
            {
                return-1;
            }

            else
             {
            for(int i=l;i<l+k;i++)
                if(st[i]=='-')
                    st[i]='+';
                else
                    st[i]='-';
             }
        }
    }
    return c;
}
int main()
{
    int p;
    cin>>p;
    for(int i=0;i<p;i++)
    {
        int l=pancakes();
        if(l==-1)
            cout<<"Case #"<<(i+1)<<": "<<"IMPOSSIBLE"<<"\n";
        else
        cout<<"Case #"<<(i+1)<<": "<<l<<"\n";
    }
}

