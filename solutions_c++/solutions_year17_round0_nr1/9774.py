#include <iostream>
#include <string>
using namespace std;

int main() {
	int t,l,m;string s;
	cin>>t;int tt=0;
	while(t--)
	{
		cin>>s>>m;
		l=s.length();
		int flag=0,x=0,br=0;
		int tot=0;tt++;
		cout<<"Case #"<<tt<<": ";
		for(int i=0;i<l;i++)
		{
			
			if(s[i]=='-'){x++;}
			else if(x!=0&&s[i]=='+'){if(flag==0)flag=2;x++;}
			//else if(flag==2&&s[i]=='-'){br=-1;break;}
			if(x==m)
			{	
			    int index=i;
				for(int j=i-m+1;j<=i;j++)
				if(s[j]=='-')s[j]='+';
				else if(index==i){index=j-1;s[j]='-';}
				else {s[j]='-';}
				i=index;
				tot++;
				x=0;flag=0;
			}
		}
		for(int i=0;i<l;i++)if(s[i]=='-'){br=-1;break;}
		if(br==-1||(flag==1&&x!=0))cout<<"IMPOSSIBLE\n";
		else cout<<tot<<endl;
	}
	return 0;
}