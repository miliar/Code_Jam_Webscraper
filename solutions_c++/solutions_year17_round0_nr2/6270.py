#include <bits/stdc++.h>
#define LL long long
using namespace std;
int main(void) {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
    {
        string num;
        cin>>num;
        int i;
        for(i=1;i<num.length();i++)
            if(num[i]<num[i-1])
                {
                    i--;
                    break;
                }
        if(i==num.length())
        {
            cout<<"Case #"<<j<<": "<<num<<endl;
            continue;
        }
        while(i&&num[i]==num[i-1])
            i--;
        num[i]--;
        for(int k=i+1;k<num.length();k++)
            num[k]='9';
        if(num[0]=='0')
            cout<<"Case #"<<j<<": "<<num.substr(1,string::npos)<<endl;
        else
            cout<<"Case #"<<j<<": "<<num<<endl;
    }
	return 0;
}

