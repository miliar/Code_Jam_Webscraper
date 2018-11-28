#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        string S;cin>>S;
        int s=S.size();
        int pos=s;
        for(int i=1;i<s;i++)
        {
            if(S[i]<S[i-1])
            {
                pos=i-1;
                while(pos>0)
                {
                    if(S[pos]==S[pos-1]) pos--;
                    else break;
                }
                break;
            }
        }
        cout<<"Case #"<<ks<<": ";
        if(pos==0&&S[0]=='1')
        {
            for(int i=1;i<s;i++) cout<<9;
        }
        else if(pos<s)
        {
            for(int i=0;i<pos;i++) cout<<S[i];
            cout<<(char)(S[pos]-1);
            for(int i=pos+1;i<s;i++) cout<<9;
        }
        else cout<<S;
        cout<<endl;
    }
	return 0;
}
