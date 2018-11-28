#include<bits/stdc++.h>
#define mpr make_pair
#define ff first
#define ss second
#define pb push_back
#define ll long long 
using namespace std;

typedef priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >, std::greater<pair<int,pair<int,int> > > > PQ;

//scanf ("%[^\n]%*c",inp);

struct Node{
	
	int x,y;
	char ch;
	Node(char ch,int x,int y):ch(ch),x(x),y(y){
		
	}
	
};


int main(){
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	
	
	int te,t=1;
	int R,C;
	scanf("%d\n",&te);
	
	while(t<=te){
		
	cin>>R>>C;
	
	char grid[R][C];
	queue<Node> Q;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cin>>grid[i][j];
			if(grid[i][j]!='?')
				Q.push(Node(grid[i][j],i,j));
		}
	}	
		
	while(Q.empty()==false){
		
		Node curr=Q.front();
		Q.pop();
		
		grid[curr.x][curr.y]=curr.ch;
		
		if(curr.x+1<R && grid[curr.x+1][curr.y]=='?'){
			Q.push(Node(curr.ch,curr.x+1,curr.y));
		}
		if(curr.x-1>=0 && grid[curr.x-1][curr.y]=='?'){
			Q.push(Node(curr.ch,curr.x-1,curr.y));
		}
		
		
	}
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			
			if(grid[i][j]!='?')
				Q.push(Node(grid[i][j],i,j));
		}
	}
	
	while(Q.empty()==false){
		
		Node curr=Q.front();
		Q.pop();
		
		grid[curr.x][curr.y]=curr.ch;
		
		if(curr.y+1<C && grid[curr.x][curr.y+1]=='?'){
			Q.push(Node(curr.ch,curr.x,curr.y+1));
		}
		if(curr.y-1>=0 && grid[curr.x][curr.y-1]=='?'){
			Q.push(Node(curr.ch,curr.x,curr.y-1));
		}
		
		
	}
	
	
	
	
	cout<<"Case #"<<t<<": "<<endl;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cout<<grid[i][j];
		}
		cout<<endl;
	}
	t++;
	}

return 0;	
}

