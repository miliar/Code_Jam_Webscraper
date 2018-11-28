#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <numeric>
#include <queue>
#include <map> 
#include <set>
#include <string>
using namespace std;
const int INF = 1e+8;

class Node{
public:
	Node(std::string s, int size,int dep);
	std::string board;
	int panSize;
	int depth;
	set<int> nowChecked;
	bool proc(int place);
	bool check();
};
Node::Node(std::string s, int size,int dep){
	board = s;
	panSize = size;
	depth = dep;
}
bool Node::proc(int place){
	//placeは区間の左端を表すものとする
	for (int i=0; i < panSize; i++){
		char looking = board[place + i];
		if (looking == '+') board[place + i] = '-';
		else board[place + i] = '+';
	}
	return true;
}
bool Node::check(){
	for (size_t i = 0; i < board.size(); i++){
		if (board[i] == '-') return false;
	}
	return true;
}

int main(){
	//方針:bfs+枝刈り、setをキーにして同じものは弾いて行く

	int caseSize;
	
	cin >> caseSize;
	for (int i = 0; i < caseSize; i++){
		set<set<int>> checked;
		queue<Node> q;
		std::string s;
		int n;
		cin >> s >> n;
		Node first(s, n, 0);
		q.push(first);
		//bfs
		bool ok = false;
		while (!q.empty()){
			Node now = q.front();
			q.pop();
			//checked.insert(now.nowChecked);
			if (now.check()){
				cout << "Case #" << i+1 << ": " << now.depth << "\n";
				ok = true;
				break;
			}
			for (int j = 0; j <= now.board.size() - now.panSize; j++){
				Node newNode = now;
				newNode.nowChecked.insert(j);
				if (checked.find(newNode.nowChecked) == checked.end()){
					checked.insert(newNode.nowChecked);
					newNode.depth += 1;
					newNode.proc(j);
					q.push(newNode);
				}
			}
		}
		if (!ok) cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
		
		
	}
	


	return 0;
}