#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;


const int M=1000+10;

struct NODE{
	char c;
	char app;
	int number;
	int appnumber;
}node[M];

char ans[3][M];

int cmp(const void *a, const void *b)
{
	return -(*(struct NODE*)a).number+(*(struct NODE*)b).number;
}

int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("B-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{		
				
		int N;
		cin>>N;
		
		for (int i=0; i<3; i++)
		{
			for (int j=0; j<N; j++)
			{
				ans[i][j]='z';
			}
		}
		
		int R,O,Y,G,B,V;
		cin>>R>>O>>Y>>G>>B>>V;
		
		cout<<"Case #"<<cnt<<": ";
		
		
		if (O+B+G+R==0)
		{
			if (Y==V)
			{
				for (int i=0; i<Y; i++)
				{
					cout<<"YV";
				}
				cout<<endl;
			}
			else
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
		}
		else
		{
			if (O+B+Y+V==0)
			{
				if (G==R)
				{
					for (int i=0; i<G; i++)
					{
						cout<<"GR";
					}
					cout<<endl;
				}
				else
				{
					cout<<"IMPOSSIBLE"<<endl;
				}
			}
			else
			{
				if (G+R+Y+V==0)
				{
					if (O==B)
					{
						for (int i=0; i<O; i++)
						{
							cout<<"OB";
						}
						cout<<endl;
					}
					else
					{
						cout<<"IMPOSSIBLE"<<endl;
					}
				}
				else
				{
					bool ok1=true;
					bool ok2=true;
					bool ok3=true;
					
					if (O>0)
					{
						if (B<O+1)
						{
							ok1=false;
						}
					}
					
					if (G>0)
					{
						if (R<G+1)
						{
							ok2=false;
						}
					}
					
					if (V>0)
					{
						if (Y<V+1)
						{
							ok3=false;
						}
					}
					
					if (ok1==false || ok2==false || ok3==false)
					{
						cout<<"IMPOSSIBLE"<<endl;
						//cout<<"e";
					}
					else
					{
						node[0].c='R';
						node[0].app='G';
						node[0].number=R-G;
						node[0].appnumber=G;
						
						node[1].c='Y';
						node[1].app='V';
						node[1].number=Y-V;
						node[1].appnumber=V;
						
						node[2].c='B';
						node[2].app='O';
						node[2].number=B-O;
						node[2].appnumber=O;
						
						qsort(node,3,sizeof(node[0]),cmp);
						
						for (int i=0; i<node[0].number; i++)
						{
							ans[0][i]=node[0].c;
						}
						
						for (int i=0; i<node[1].number; i++)
						{
							ans[1][i]=node[1].c;
						}
						
						for (int i=0; i<node[2].number; i++)
						{
							ans[2][node[0].number-1-i]=node[2].c;
						}
						
						if (node[1].number+node[2].number>=node[0].number)
						{
							bool ok[3];
							ok[0]=ok[1]=ok[2]=false;
							for (int i=0; i<node[0].number; i++)
							{
								for (int j=0; j<3; j++)
								{
									if (ans[j][i]!='z')
									{
										if (ok[j]==false)
										{
											cout<<node[j].c;
											for (int k=0; k<node[j].appnumber; k++)
											{
												cout<<node[j].app<<node[j].c;
											}
											ok[j]=true;
										}
										else
										{
											cout<<ans[j][i];
										}
									} 						
								}
							}
							cout<<endl;
						}
						else
						{
							cout<<"IMPOSSIBLE"<<endl;
						}
					}
				}
				
				
			}
			
			
		}
		
		
		
		
		
		
	}
	
	
	
	
	return 0;
	
}
