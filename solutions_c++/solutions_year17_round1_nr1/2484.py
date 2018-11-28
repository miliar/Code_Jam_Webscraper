#include<iostream>
#include<string>
#include<vector>
using namespace std;
int initiate;
int row,column;
vector<vector<char> > mat;
void parse(string input){
	int x=0;
	while(input[x]!='\0'){
		mat[initiate][x]=input[x];
		x++;
	}
	initiate++;
}
void acquire(){
	int checkRow=-1,x,y,z;
	char character;
	bool breakCheck;
	
	for(x=row-1;x>=0;x--)
	{
		for(y=0;y<column;y++)
		{
			breakCheck=true;
			if(mat[x][y]!='?')
			{
				character=mat[x][y];
				for(z=y-1;z>=0;z--)
					if(mat[x][z]=='?')
						mat[x][z]=character;
					else
					{
						breakCheck=false;
						break;
					}
				for(z=y+1;z<column;z++)
					if(mat[x][z]=='?')
						mat[x][z]=character;
					else
					{
						breakCheck=false;
						break;
					}				
				checkRow=x;
				if(breakCheck)
					break;
			}
						
		}
		if((checkRow!=-1)&&(checkRow>x))
		{
				for(int z=0;z<column;z++)
					mat[x][z]=mat[checkRow][z];
				checkRow=x;			
		}
	}
	checkRow=-1;
	for(x=0;x<row;x++)
	{
		for(y=0;y<column;y++)
		{
			breakCheck=true;
			if(mat[x][y]!='?')
			{
				character=mat[x][y];
				for(z=y-1;z>=0;z--)
					if(mat[x][z]=='?')
						mat[x][z]=character;
					else
					{
						breakCheck=false;	
						break;
					}
				for(z=y+1;z<column;z++)
					if(mat[x][z]=='?')
						mat[x][z]=character;
					else 
					{
						breakCheck=false;
						break;
					}
				checkRow=x;
				if(breakCheck)
					break;
			}
						
		}
		if((checkRow!=-1)&&(checkRow<x))
		{
				for(int z=0;z<column;z++)
					mat[x][z]=mat[checkRow][z];
				checkRow=x;			
		}
	}					
	
}

int main()
{
	int testCaseCount,x=0,y=0;
	cin>>testCaseCount;
	int caseCount=0;
	while(testCaseCount--)
	{
		cin>>row>>column;
		string input;
		vector<vector<char> > reference(row,vector<char>(column,' '));
		mat=reference;
		x=0;
		while(x<row)
		{
			cin>>input;
			parse(input);
			x++;
		}
		caseCount++;
		cout<<"Case #"<<caseCount<<":\n";
		initiate=0;
		acquire();
		x=0;
		while(x<row)
		{
			y=0;
			while(y<column)
			{
				cout<<mat[x][y];
				y++;
			}
			x++;	
			cout<<"\n";
		}
	}
	return 0;
}
