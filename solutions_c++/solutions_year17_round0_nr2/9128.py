#include<iostream>
#include<cstring>
using namespace std;
main()
{
	ios_base::sync_with_stdio(0);
	int testy,pocz,kon;
	char n[25];
	cin>>testy;
	for(int test=1;test<=testy;test++)
		{
		cin>>n;	
		pocz=0;
		kon=strlen(n);
		for(int a=0,b=strlen(n);a<b-1;a++)
			{
			if((int)n[a]>(int)n[a+1])
				{
				if(a==0)
					{
					if(n[a]=='1')
						{
						pocz=1;
						for(int c=1;c<b;c++)n[c]='9';
						}
					else
						{
						pocz=0;
						n[0]=(char)((int)n[0]-1);
						for(int c=1;c<b;c++)n[c]='9';
						}
					}
				else
					{
					int c=a;
					for(;c>0;c--)
						if((int)n[c]!=(int)n[c-1])break;
					if(c==0)
						{
						if(n[0]=='1')pocz=1;
						else
							{
							pocz=0;
							n[0]=(char)((int)n[0]-1);
							}
						for(int c=1;c<b;c++)n[c]='9';
						}
					else
						{
						pocz=0;
						n[c]=(char)((int)n[c]-1);
						for(c++;c<b;c++)n[c]='9';
						}
					}
				kon=b;
				break;
				}
			}
		cout<<"Case #"<<test<<": ";
		for(int a=pocz;a<kon;a++)cout<<n[a];
		cout<<endl;
		}
	return 0;
}
