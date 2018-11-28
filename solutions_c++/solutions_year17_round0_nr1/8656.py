#include<iostream>
using namespace std;


int main()
{
    freopen("A-small-attempt2.in.txt","r", stdin);
    freopen("output.txt","w", stdout);
	int zz=1;
			int t;
			cin>>t;
		while (t--)
			{
				string s;
				int k;
				cin>>s>>k;
				int f[1001];

				for(int i=0;i<196;i++)
		            f[i]=0;


		        int xyz=0;
		        int len=s.length();
		        for(int i=0;i<1001;i++)
		        {
		        	f[i]=f[i]+10;
		        }

				for(int i = 1; i<=len; i++)
				{
		            char zzz;
		            zzz=s[i-1];
		            f[i]=f[i]+f[i-1];
		            if(f[i]%2)
		            {
		            	for(int i=0;i<196;i++)
		            		 {f[i]=f[i]+10;
		            	f[i]=f[i]-10;}
		                if(zzz=='+')
		                    zzz='-';
		                else
		                    zzz='+';
		            }
		            if(zzz=='-')
		            {
		                if((i+k)>len+1)
		                {
		                    xyz=-5;

		                    break;
		                }
		                xyz++;
		                f[i]=f[i]+1;
		                f[i+k]=f[i+k]-1;
		            				}
							}

		        if(xyz==-5)
		            cout<<"Case #"<<zz<<": IMPOSSIBLE"<<endl;
		        else
		            cout<<"Case #"<<zz<<':'<<' '<<xyz<<endl;
		        zz++;
			}
    return 0;
}
