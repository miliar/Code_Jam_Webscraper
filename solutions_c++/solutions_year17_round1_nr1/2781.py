#include <bits/stdc++.h>

using namespace std;

int main()
{
	int r,c,u,t,i,j,k,flag,updated = 1;
	char a[30][30];
	int firstleft[30],firstright[30],firsttop[30],firstbottom[30],count[30];
	cin>>t;
	for(u=0;u<t;u++)
	{
		cin>>r>>c;
		updated = 1;
		memset(a,0,sizeof a);
		memset(count,0,sizeof count);
		memset(firsttop,0,sizeof firsttop);
		memset(firstbottom,0,sizeof firstbottom);
		memset(firstright,0,sizeof firstright);
		memset(firstleft,0,sizeof firstleft);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cin>>a[i][j];
			}
		}
		for(k='A';k<='Z';k++)
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					if(a[i][j] == k)
					{
						count[a[i][j]-'A'] = 1;
						firsttop[a[i][j]-'A'] = i;
						break;
					}
				}
			}
			for(i=r-1;i>=0;i--)
			{
				for(j=0;j<c;j++)
				{
					if(a[i][j] == k)
					{
						firstbottom[a[i][j]-'A'] = i;
						break;
					}
				}
			}
			for(j=0;j<c;j++)
			{
				for(i=0;i<r;i++)
				{
					if(a[i][j] == k)
					{
						firstleft[a[i][j]-'A'] = j;
						break;
					}
				}
			}
			for(j=c-1;j>=0;j--)
			{
				for(i=0;i<r;i++)
				{
					if(a[i][j] == k)
					{
						firstright[a[i][j]-'A'] = j;
						break;
					}
				}
			}	
		}
		for(k='A';k<='Z';k++)
		{
			if(count[k-'A'])
			{
				for(i=firsttop[k-'A'];i<=firstbottom[k-'A'];i++)
				{
					for(j=firstleft[k-'A'];j<=firstright[k-'A'];j++)
					{
						a[i][j] = k;
					}
				}
			}		
		}
		while(updated)
		{
			updated = 0;
			for(k = 'A';k<='Z';k++)
			{
				if(count[k-'A'])
				{
					if(firsttop[k-'A']>=1) 
					{
						flag = 1;
						i=firsttop[k-'A']-1;
							for(j=firstleft[k-'A'];j<=firstright[k-'A'];j++)
							{
								if(a[i][j]!='?')
									flag = 0;
							}
						if(flag)
						{
							updated = 1;
							for(j=firstleft[k-'A'];j<=firstright[k-'A'];j++)
							{
								a[i][j] = k;
							}
							firsttop[k-'A']--;
						}	
						
					}
					if(firstbottom[k-'A']<r-1) 
					{
						flag = 1;
						i=firstbottom[k-'A']+1;
							for(j=firstleft[k-'A'];j<=firstright[k-'A'];j++)
							{
								if(a[i][j]!='?')
									flag = 0;
							}
						if(flag)
						{
							updated = 1;
							for(j=firstleft[k-'A'];j<=firstright[k-'A'];j++)
							{
								a[i][j] = k;
							}
							firstbottom[k-'A']++;
						}	
						
					}	
					if(firstright[k-'A']<c-1) 
					{
						flag = 1;
						j=firstright[k-'A']+1;
							for(i=firsttop[k-'A'];i<=firstbottom[k-'A'];i++)
							{
								if(a[i][j]!='?')
									flag = 0;
							}
						if(flag)
						{
							updated = 1;
							for(i=firsttop[k-'A'];i<=firstbottom[k-'A'];i++)
							{
								a[i][j] = k;
							}
							firstright[k-'A']++;
						}		
					}	
					if(firstleft[k-'A']>=1) 
					{
						flag = 1;
						j=firstleft[k-'A']-1;
							for(i=firsttop[k-'A'];i<=firstbottom[k-'A'];i++)
							{
								if(a[i][j]!='?')
									flag = 0;
							}
						if(flag)
						{
							updated = 1;
							for(i=firsttop[k-'A'];i<=firstbottom[k-'A'];i++)
							{
								a[i][j] = k;
							}
							firstleft[k-'A']--;
						}		
					}
				}	
			}
		}
		cout<<"Case #"<<u+1<<":\n";
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cout<<a[i][j];
			}
			cout<<"\n";
		}
	}

	return 0;
}