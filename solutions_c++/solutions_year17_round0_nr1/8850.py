#include <iostream>
#include<string.h>
using namespace std;

/*int length(char *s)
{
    int i,len=0;
    for(i=0;s[i]!='\0';i++)
        len++;
    return len;

}*/

int all(string s)
{
    for(int i=0;s[i]!='\0';i++)
    {
        if(s[i]=='-')
            return 0;
    }
    return 1;
}

int main()
{
   	int t;
	cin>>t;
	int k;
	string s;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		cin>>k;
		cout << "Case #" << i << ": ";
		int flip=0;
		//cout<<"s::  "<<s;
		//cout<<" K :: "<<k;
		char pros='+';
		char cons='-';
		char ch[k];
		int len=s.length();
		for(int j=0;j<len;j++)
		{
			if(s[j]!=pros)
			{
				int num=0;
				for(int x=0;x<k;x++)
				{
					if(s[j+x]==cons)
						num++;
				}
				if(num==k)
				{
					for(int x=0;x<k;x++)
					{
						s[j+x]='+';
					}
					flip++;
					//cout<<"flip "<<flip<<" "<<s;
					j=j+k-1;
				}
				else if(j<=(len-k))
				{
					int y;
					for(y=0;y<k;y++)
					{
						ch[y]=s[j+y];
					}
					for(y=0;y<k;y++)
					{
						if(s[j+y]==pros)
						    s[j+y]=cons;
						else
						    s[j+y]=pros;
					}
					flip++;
					//cout<<"flip "<<flip<<" "<<s<<endl;
				}
			}


		}
		
		if(all(s))
            cout<<flip<<endl;
        else 
            cout<<"IMPOSSIBLE\n";
	}
    return 0;
}
