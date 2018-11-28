#include<iostream>
#include<vector>
#include <queue>
#include<fstream>
using namespace std;

class node{
	public:
	int moves;
	string state;
	//node * next;
	node(){
		moves=0;
	//	next=NULL;
	}
	node(string s,int m){
		state=s;
		moves=m;
	}
	bool operator<( const node & n) const {
		return moves>n.moves;
	}
	
	bool operator<=(const node & n) const {
		return moves>=n.moves;
	}
	bool operator>( const node & n) const {
		return moves<n.moves;
	}
	bool operator>=( const node & n)const{
		return moves<=n.moves;
	}
	bool operator==(const node & n) const{
		return moves==n.moves;
	}
};

vector<vector<string> > states;
int hash_size=101;

int calculate_hash(string st){
	int sum=0;
	for(int i=0;i<st.length() && i<10;i++){
		if(st[i]=='+'){
			sum++;	
		}
		
	}
	int hashvalue=sum%hash_size;
	return hashvalue;
}

bool check_visited(string st,int & hash_value){
	
	hash_value=calculate_hash(st);
	for(int j=0;j<states[hash_value].size();j++){
		if(states[hash_value][j]==st){
			return true;
		}
		
	}
	
	return false;
}

string flipbuns(string st,int pansize,int index){
	
	for(int i=0;i<pansize;i++){
		if(st[i+index]=='+'){
			st[i+index]='-';
		}
		else if(st[i+index]=='-'){
			st[i+index]='+';
		}	
	}
	return st;
}
////////////////////////////////////////////////
int leastmoves(string pancake, int pansize,string desired) {
	 priority_queue<node> pq;
	 
	 
	 
	
	 pq.push(node(pancake,0));
	
	 while (!pq.empty() ) {
		  node top = pq.top();
		  pq.pop();
		
				//	cout<<"test0\n";
	      int hash_value;
		  // Make sure we don't visit the same configuration twice
		  if (check_visited(top.state,hash_value)) {
					 // 	cout<<"test1\n";
					  //	cout<<top.state<<endl;
			  continue;	
		  }
		  
		  states[hash_value].push_back(top.state);
					// cout<<top.state<<endl;
		
		  
		  if (top.state==desired){
		  //	cout<<"test2\n";
		  	return top.moves;
		  }
			
		   
		   
		   for (int i = 0; i <= top.state.length()-pansize; i++){
		   		string newstate=flipbuns(top.state,pansize,i);
		   		pq.push(node(newstate,top.moves+1));
		   	
		   }
		
		  
	 }
	 return -1;
}









////////////////////////////////////////////////

int main(){
	//states=new nodes* [hash_size];
	ifstream ifs ("a.in");
	ofstream ofs("b.out");
	if(ifs.is_open() && ofs.is_open()){
		int testcases=0;
		ifs>>testcases;
		
		for(int i=0;i<hash_size;i++){
				vector<string> s;
				states.push_back(s );
		}
		
		for(int tno=0;tno<testcases;tno++){
			
			
			
			string inputs1;
			ifs>>inputs1;
			int pansize=0;
			ifs>>pansize;
			
			string desired="";
			for(int t=0;t<inputs1.length();t++){
				desired+='+';
			}
			int result=leastmoves(inputs1,pansize,desired);
			if(result!=-1){
				ofs<<"Case #"<<tno+1<<": "<< result<<endl;
				cout<<"Case #"<<tno+1<<": "<< result<<endl;
			}
			else{
				ofs<<"Case #"<<tno+1<<": "<< "IMPOSSIBLE"<<endl;
				cout<<"Case #"<<tno+1<<": "<< "IMPOSSIBLE"<<endl;
			}
			
			
			for(int i=0;i<hash_size;i++){
				states[i].clear();
			}
		//	states.clear();
			
			
		}
		
	}
	
	return 0;
}
