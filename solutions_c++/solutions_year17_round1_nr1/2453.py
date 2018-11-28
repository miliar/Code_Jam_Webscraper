#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;
int main()
{
	int T;
	int R,C;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		bool uk = false;
		cin>>R>>C;
		vector<string> v(R);
		for(int j=0;j<R;j++)
		{
			cin>>v[j];
			if(uk == false && count(v[j].begin(),v[j].end(),'?')!=0)
			{
				uk = true;//input contains atleast one ?
			}
			if(uk == true && count(v[j].begin(),v[j].end(),'?')!=C)//row contains a ? and entire row is not ?
			{
				for(int k=1;k<C-1;k++)
				{
					if(v[j][k]=='?')
					{
						if(v[j][k-1]!='?')
						{
							
							v[j][k] = v[j][k-1];			
						}
						else
						if(v[j][k+1]!='?')
						{
							v[j][k] = v[j][k+1];
							int p=k;
							while(--p>=0)
							{
								if(v[j][p]=='?')
									v[j][p] = v[j][p+1];
							}
						}
					}					
				}
				if(v[j][C-1]=='?')//last char is a ?, copy second last char to last char
					v[j][C-1] = v[j][C-2];
				if(v[j][0] == '?')
				{					
					v[j][0] = v[j][1];
				}
			}						
		}
		if(uk == false)//no ? in entire input
		{
			cout<<"Case #"<<i<<":\n";
			for(auto e: v)
				cout<<e<<"\n";
		}
		else if(uk == true && R==1)
		{
			cout<<"Case #"<<i<<":\n";
			for(auto e: v)
				cout<<e<<"\n";
		}
		else if(uk == true)
		{
			for(int x = 0;x<R;x++)
			{
				if(count(v[x].begin(),v[x].end(),'?')==C && x<=R-2)
				{
					if(x!=0 && count(v[x-1].begin(),v[x-1].end(),'?')==0)
						v[x] = v[x-1];
					else
					{
						int p = x;
						while(p>=0)
						{
							if(count(v[p].begin(),v[p].end(),'?')==C)
								v[p] = v[p+1];
							--p;
						}
					}
				}
			}
			if(count(v[R-1].begin(),v[R-1].end(),'?')==C)
				v[R-1] = v[R-2];
			cout<<"Case #"<<i<<":\n";
			for(auto e: v)
				cout<<e<<"\n";
		}
		
	}
}
