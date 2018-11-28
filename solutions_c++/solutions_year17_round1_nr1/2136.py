#define LOCAL
#include<iostream>
using namespace std; 

int main()
{
	#ifdef LOCAL
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<":"<<endl;
		int r,c;
		cin>>r>>c;
		char cake[r][c];
		for(int row=0;row<r;row++)
			cin>>cake[row];
		bool isPrevEmptyRow=true;
		int firstNonEmptRow=-1;
		int prevNonEmptRow=-1;
		for(int row=0;row<r;row++){

			bool isEmpRow=true;
			int rowFirstInd=0;
			char rowFirstChar='?';
			for(int col=0;col<c;col++){
				if(cake[row][col]!='?'){
					isEmpRow=false;
					isPrevEmptyRow=false;
					prevNonEmptRow=row;
					if(firstNonEmptRow==-1)
						firstNonEmptRow=row;
					rowFirstInd=col;
					rowFirstChar=cake[row][col];
					break;
				}
			}
			if(!isEmpRow){
				for(int col=0;col<c;col++){
					if(cake[row][col]=='?'){
						cake[row][col]=rowFirstChar;
					}
					else{
						if(cake[row][col]!=rowFirstChar){
							rowFirstChar=cake[row][col];
						}
					}
				}
			}

			else{
				if(!isPrevEmptyRow){//copy the before one
					for(int col=0;col<c;col++){
						cake[row][col]=cake[prevNonEmptRow][col];
					}
				}
			}
		}
		//first
		int row=firstNonEmptRow-1;
		while(row>=0){
			for(int col=0;col<c;col++){
				cake[row][col]=cake[firstNonEmptRow][col];
			}
			row--;
		}
		for(int row=0;row<r;row++)
			{for(int col=0;col<c;col++)
				cout<<cake[row][col];
			cout<<endl;}
	}
	return 0;
}
