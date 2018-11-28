#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cout<<"Case #"<<z<<":\n";
		int r,c;
		cin>>r>>c;
		char g[r][c];
		for(int i=0;i<r;i++)
		{
				cin>>g[i];
		}
		/*for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<g[i][j];
			}
			cout<<endl;
		}*/
		int flg=0,pos=-1;
		for(int i=0;i<r;i++)
		{
			flg=0;
			for(int j=0;j<c;j++)
			{
				if( g[i][j]!='?' )
				{
					if(j==0)
					{
						char ch=g[i][j];
						j++;
						for(;j<c;j++)
						{
							if(g[i][j]!='?')
							{
								j--;
								break;
							}
							g[i][j]=ch;
						}
						flg=1;
					}
					else
					{
						if(flg==1)
						{
							char ch=g[i][j];
							j++;
							for(;j<c;j++)
							{
								if(g[i][j]!='?')
								{
									j--;
									break;
								}
								g[i][j]=ch;
							}
						}
						if(flg==0)
						{
							char ch=g[i][j];
							//cout<<"omi "<<ch;
							int tmp;
							for(tmp=0;tmp<j;tmp++)
							{
								/*if(g[i][j]!='?')
								{
									j--;
									break;
								}*/
								g[i][tmp]=ch;
							}
							j++;
							for(;j<c;j++)
							{
								if(g[i][j]!='?')
								{
									j--;
									break;
								}
								g[i][j]=ch;
							}
						}
						flg=1;
					}
				}
			}
			if(flg==0)
			{
				for(int j=0;j<c;j++)
				{
					if(i!=0 && pos!=i-1)
						g[i][j]=g[i-1][j];
					else
						pos=i;
				}
			}
		}
		for(int i=pos;i>=0;i--)
		{
			for(int j=0;j<c;j++)
			{
				g[i][j]=g[i+1][j];
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<g[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
