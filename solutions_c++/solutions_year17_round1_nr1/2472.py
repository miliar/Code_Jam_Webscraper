#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int T;
	int R, C;
	string inpch;
	bool flag;

  freopen ("A-large.in","r",stdin);
  freopen("A-large-output.out", "w", stdout);

//Getting number of times
	scanf("%d", &T);


	//For each number
	for(int t=1;t<=T;t++){
		cin >> R >> C;
		vector<int> count(C,0);
		vector<int> start(C,R);
		vector < vector<char> > ch(R, vector<char> ( C, '?' ) );
		vector < vector<char> > result(R, vector<char> ( C, '?' ) );
		for(int r=0; r<R; r++){
			cin >> inpch;	
			for(int c=0; c<C; c++)
				ch[r][c] = inpch[c];				
		}

		for(int c=0; c<C; c++)
			for(int r=0; r<R; r++)
				if(ch[r][c] != '?')
					count[c]++;

		for(int c=0; c<C; c++){
			if(count[c] == 0)
				continue;
			for(int r=0; r<R; r++)
				if(ch[r][c] != '?'){
					start[c] = r;
					for(int rr=r; rr>=0; rr--){
						ch[rr][c] = ch[r][c];
						for(int cc=c+1; cc<C && count[cc]==0; cc++)
							ch[rr][cc] = ch[r][c];
					}
					break;
				}
		}

		for(int c=0; c<C; c++)
			for(int r=start[c]+1; r<R; r++){
				if(ch[r][c] == '?'){
					ch[r][c] = ch[r-1][c];
				}	
				for(int cc=c+1; cc<C && count[cc]==0; cc++)
					ch[r][cc] = ch[r][c];
				
				}
		
		int c=0;
		for(; c<C && count[c]==0 ; c++);
			
		if(c!=0){
			for(int r=0; r<R; r++){
				for(int cc=c-1; cc>=0; cc--)
					ch[r][cc] = ch[r][c];
			}
		}		


//		for(int c=0; c<C; c++)
//			cout << count[c] << ' ';				
		cout << "Case #"<< t << ":\n";
 		for(int r=0; r<R; r++){
		for(int c=0; c<C; c++)
			cout << ch[r][c];				
		cout << '\n';
		}
	}

return 0;
}