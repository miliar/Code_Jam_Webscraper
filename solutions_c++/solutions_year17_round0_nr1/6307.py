#include <bits/stdc++.h>
#define LL long long
using namespace std;
int minpos(string &str,int pos)
{
    for(int i=pos;i<str.size();i++)
        if(str[i]=='-')
          return i;
    return -1;
}
int flip(string &str,int pos,int k)
{
   if(str.size()-pos<k)
        return 0;
   for(int i=0;i<k;i++)
    if(str[i+pos]=='+')
      str[i+pos]='-';
    else
      str[i+pos]='+';
    return 1;
}
int main(void) {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
    {
        string str;
        int k;
        cin>>str>>k;
        int changes=0;
        int i;
        for(i=0;i<str.size();i++)
        {
            //cout<<i<<" "<<changes<<endl;
            int pos;
            pos=minpos(str,i);
            if(pos==-1)
            {
                cout<<"Case #"<<j<<": "<<changes<<endl;
                break;
            }
            else
            {
                if(!flip(str,pos,k))
                {
                    cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
                    break;
                }
                changes++;
            }
        }
        if(i==str.length())
            cout<<"Case #"<<j<<": "<<changes<<endl;
    }
	return 0;
}

