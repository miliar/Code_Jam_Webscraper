#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int t,k;
    cin>>t;
    char s[1002];
    for(int i=1;i<=t;i++)
    {
		int cnt=0;
        cin>>s>>k;
        int j;
        for(j=0;j<strlen(s);j++)
        {
            if(s[j]!='+')
                break;
        }
        if(j==strlen(s))
            cout<<"Case #"<<i<<": "<<0<<endl;
		else
       {
        for(j=0;j<strlen(s);j++)
        {
            if(s[j]=='-')
            {
				for(int m=0;(m<k)&&((j+k-1)<strlen(s));m++)
				{
					if(s[j+m]=='-')
						s[j+m]='+';
					else 
						s[j+m]='-';
				}
				cnt++;
            }
        }
		int p;
        for(p=0;p<strlen(s);p++)
        {
            if(s[p]!='+')
				break;
        }
        if(p!=strlen(s))
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
    }
    return 0;
}
