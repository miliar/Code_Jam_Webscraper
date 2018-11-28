#include <bits/stdc++.h>
using namespace std;
int T,R,C; string S; char A[30][30];
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>R>>C;
		for(int i=0; i<R; i++)
		{
			cin>>S;
			for(int j=0; j<C; j++)
			A[i][j]=S[j];
		}
		int first_fill=-1;
		for(int i=0; i<R; i++)
		{
			//Lets check whether this row has atleast one character
			int flag=0;
			for(int j=0; j<C; j++)
			{
				if(A[i][j]!='?')
				{
					flag=1;
					break;
				}
			}
			//if(flag==0)continue;
			if(first_fill!=-1 && flag==0)
			{
				//previous row is filled
				for(int j=0; j<C; j++)
				{
					A[i][j]=A[i-1][j];
				}
				continue;
			}
			if(flag==0 && first_fill==-1)continue;
			
			/*Lets fill this row now*/
			for(int j=0; j<C; j++)
			{
				if(A[i][j]=='?')
				{
					char x='-';
					for(int k=j+1; k<C; k++)
					{
						if(A[i][k]!='?')
						{
							x=A[i][k];
							break;
						}
					}
					if(x=='-')
					{
						for(int k=j-1; k>=0; k--)
						{	
							if(A[i][k]!='?')
							{
								x=A[i][k];
								break;
							}
						}	
					}
					A[i][j]=x;
				}
			}
			if(first_fill==-1)
			{
				first_fill=i;
				//fill the top rows;
				for(int k=i-1; k>=0; k--)
				{
					for(int j=0; j<C; j++)
					{
						A[k][j]=A[k+1][j];
					}
				}
			}
		}
		cout<<"Case #"<< cases << ":\n";
		for(int i=0; i<R; i++)
		{
			for(int j=0 ; j<C; j++)cout<<A[i][j];
			cout<<endl;
		}
	}
}
