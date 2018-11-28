#include <iostream>
using namespace std;

int R,C;
char cakes[30][30];
bool finished[30];

void hfill(int row,int ls,int rs){
	int firstcol=-1;
	for(int j=ls;j<rs;j++)
		if(cakes[row][j]!='?')
		{
			firstcol=j;break;
		}

	for(int j=firstcol-1;j>=ls;j--)
		cakes[row][j]=cakes[row][j+1];
	for(int j=firstcol+1;j<rs;j++)
		if(cakes[row][j]=='?')
			cakes[row][j]=cakes[row][j-1];
}
void fill(int row,int ls,int rs,char c){
	for(int i=ls;i<rs;i++)
		cakes[row][i]=c;
}

int onecase()
{
	cin>>R>>C;
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
			cin>>cakes[i][j];
	}
	for(int i=0;i<R;i++)
		finished[i]=false;
	
	//first row, where?
	int firstrow=-1;
	for(int i=0;i<R;i++){
		bool cond=false;
		for(int j=0;j<C;j++)
			if(cakes[i][j]!='?'){
				firstrow=i;
				cond=true;
				break;
			}
		if(cond)
			break;
	}
	hfill(firstrow,0,C);
	//done firstrow

	//others, going upward
	for(int i=firstrow;i>=0;i--){
		int ei=i+1;
		int ls=0;int rs=0;
		while(ls<C){
			//sweep from left
			while(cakes[ei][rs]==cakes[ei][ls] && rs<C)rs++;
			bool cond=false;
			for(int j=ls;j<rs;j++)
				if(cakes[i][j]!='?')cond=true;
			if(cond)
				hfill(i,ls,rs);
			else
				fill(i,ls,rs,cakes[ei][ls]);
			//advance to next seg
			ls=rs;
		}
	}

	//others, going downward
	for(int i=firstrow+1;i<R;i++)
	{
		int ei=i-1;
		int ls=0;int rs=0;
		while(ls<C){
			//sweep from left
			while(cakes[ei][rs]==cakes[ei][ls] && rs<C)rs++;
			bool cond=false;
			for(int j=ls;j<rs;j++)
				if(cakes[i][j]!='?')cond=true;
			if(cond)
			{
				//cout<<"hfill:"<<i<<":"<<ls<<"-"<<rs<<endl;
				hfill(i,ls,rs);
			}
			else{
				//cout<<"copy:"<<i<<":"<<ls<<"-"<<rs<<"("<<cakes[ei][ls]<<endl;
				fill(i,ls,rs,cakes[ei][ls]);
			}
			//advance to next seg
			ls=rs;
		}
	}



	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
			cout<<cakes[i][j];
		cout<<endl;
	}
	return 0;
}

int main(){
	//onecase();return 0;

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<":"<<endl;
		onecase();
	}
	return 0;
}