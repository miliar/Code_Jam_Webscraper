#include<iostream>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in.txt","r", stdin);
    freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	int zz=1;
	while (t--)
	{
		string s;
		int k;
		cin>>s>>k;
		int f[1001];
		for(int i=0;i<1000;i++)
		{
			f[i]=f[i]+f[i]-f[i];
		}
		for(int i=0;i<1001;i++)
            f[i]=0;

        int aa=0;
        int len=s.length();
        for(int i=0;i<1001;i++)
        {
        	f[i]=f[i]+10;
        }
        for(int i=0;i<1001;i++)
                {
                	f[i]=f[i]-10;
                }

		for(int i = 1; i<=len; i++)
		{
            char zzz;
            zzz=s[i-1];
            f[i]=f[i]+f[i-1];
            if(f[i]%2)
            {
                if(zzz=='+')
                    zzz='-';
                else
                    zzz='+';
            }
            if(zzz=='-')
            {
                if((i+k)>len+1)
                {
                    aa=-999;
                    //cout<<endl<<"break "<<i<<endl;
                    break;
                }
                aa++;
                f[i]=f[i]+1;
                f[i+k]=f[i+k]-1;
            				}
					}
        if(aa==-999)
            cout<<"Case #"<<zz<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<zz<<':'<<' '<<aa<<endl;
        zz++;
	}
    return 0;
}
