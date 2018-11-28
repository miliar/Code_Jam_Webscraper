#include<bits/stdc++.h>
using namespace std;
bool cek(string s,long long len)
{
    long long i,xx;
    xx=s[0];
    for(i=1;i<len;++i)
    {
        if(s[i]<xx)
        {
            return 0;
        }

        xx=s[i];
    }
    return 1;
}
int main()
{
    ifstream cin("mkultra.in");
    ofstream cout("mkultra.out");
    long long i,len,T,it,we;
    long long coy=100;
    //cout<<cek("120",3);
    cin>>T;
    we=0;
    while(T--)
    {
        cout<<"Case #"<<++we<<": ";
        string s;
        vector<char> news;
        coy=100;
        cin>>s;
        len=s.length();
        if(cek(s,len))
        {
            cout<<s;//<<endl;
            goto sana;
        }

        while(coy--)
        {
            for(i=0; i<len-1; ++i)
            {
                //cout<<s[i]<<' '<<s[i+1]<<endl;
                if(s[i]>s[i+1])
                {

                    s[i]--;
                    for(it=i+1;it<len;++it)
                    {

                        s[it]='9';
                    }
                    if((s[i]=='0')and(i==0))
                    {

                       for(it=0;it<len-1;++it)
                       {
                           cout<<9;
                       }

                       goto sana;
                    }
                }
            }
            //cout<<s<<endl;
        }
        cout<<s;
        sana:;
        cout<<"\n";
    }
}
