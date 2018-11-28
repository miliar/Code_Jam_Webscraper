//#include <iostream>
//#include <algorithm>
//#include <vector>
//#include<stack>
//
//using std::vector;
//using std::pair;
//using std::stack;
//
//vector<bool>visited;
//vector<bool>processed;
//vector<int>post;
//vector<int>pre;
//stack<int>s;
//
//int clk = 1;
//void explore(vector<vector<int> > &adj, int v){
//	visited[v] = true;
//	pre[v] = clk++;
//	for (int i = 0; i < adj[v].size(); i++){
//		if (!visited[adj[v][i]]){
//			explore(adj, adj[v][i]);
//		}
//
//	}
//
//	post[v] = clk++;
//	s.push(v);
//
//}
//void DFS(vector<vector<int> > &adj){
//	for (int i = 0; i < adj.size(); i++){
//		if (!visited[i]){
//			explore(adj, i);
//		}
//	}
//
//
//}
//
//
//void dfs(vector<vector<int> > &adj, vector<int> &used, vector<int> &order, int x) {
//	//write your code here
//}
//
//vector<int> toposort(vector<vector<int> >& adj) {
//	//vector<int> used(adj.size(), 0);
//	//vector<int> order;
//	DFS(adj);
//	vector<int>order(adj.size());
//	for (int i = 0; i < adj.size(); i++){
//		order[i] = s.top();
//		s.pop();
//	}
//	//write your code here
//	return order;
//}
//
//int main() {
//	size_t n, m;
//	std::cin >> n >> m;
//
//	vector<vector<int> > adj(n, vector<int>());
//	visited.resize(n);
//	post.resize(n);
//	pre.resize(n);
//
//	for (size_t i = 0; i < m; i++) {
//		int x, y;
//		std::cin >> x >> y;
//		adj[x - 1].push_back(y - 1);
//	}
//	for (int i = 0; i < n; i++){
//		visited[i] = false;
//		processed[i] = false;
//	}
//	vector<int> order = toposort(adj);
//	for (size_t i = 0; i < order.size(); i++) {
//		std::cout << order[i] + 1 << " ";
//	}
//	system("pause");
//}
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int num = 0;
int numberOfFlips(string seq, int s){
	//static int num = num_global;
	int l = seq.length();

	if (l < s){
		for (int i = 0; i < l; i++){
			if (seq[i] != '+')
				return -1;
		}
		return num;
	}
	if (seq[0] == '+')
		return numberOfFlips(seq.substr(1), s);

	if (seq[0] == '-'){
		seq = seq.substr(1);
		for (int i = 0; i < s - 1; i++){
			seq[i] = (seq[i] == '+') ? '-' : '+';
		}
		num++;
		return numberOfFlips(seq, s);
	}


}
vector<int> solve(vector<pair<string, int>>&vec){
	vector<int>result(vec.size());
	for (int i = 0; i < vec.size(); i++){
		num = 0;
		result[i] = numberOfFlips(vec[i].first, vec[i].second);
	}

	return result;
}

int main(){
	freopen("in.txt", "r", stdin);

	
	freopen("out.txt", "w", stdout);
	int n;
	
	cin >> n;
	vector<pair<string, int>>vec(n);
	for (int i = 0; i < n; i++){
		cin >> vec[i].first >> vec[i].second;
	}
	vector<int>result = solve(vec);
	//output
	for (int i = 0; i < n; i++){
		cout << "Case #"<<i+1<<": ";
		if (result[i] != -1)
			cout << result[i] << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
	/*string x; int n;
	cin >> x >> n;
	cout << numberOfFlips(x, n);

	system("pause");*/
}