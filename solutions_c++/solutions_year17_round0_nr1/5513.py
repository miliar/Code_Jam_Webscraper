
#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
	int main()
	{
	    freopen("A-large.in","rt",stdin);
	    freopen("A-lout.txt","wt",stdout);
		int i=0,j=0;
		char s[1005];
		int t,l,k;
		cin>>t;
		for(l=0;l<t;l++)
		{
			cin>>s;
			cin>>k;
			//cout<<s;
			int cnt=0;
			for(i=0;s[i+k-1]!='\0';i++)
			{
				if(s[i]=='+')           //---+-++-
					continue;
                cnt++;
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
                    else
						s[j]='+';

				}
                //cout<<s<<endl;
			}
			for(j=0;s[j]!='\0';j++)
            {
                if(s[j]=='-')
                    break;
            }
            if(s[j]=='\0')
            {
                cout<<"Case #"<<(l+1)<<": "<<cnt<<endl;
            }
            else
                cout<<"Case #"<<(l+1)<<": "<<"IMPOSSIBLE"<<endl;

		}
		getch();
        return 0;
	}
